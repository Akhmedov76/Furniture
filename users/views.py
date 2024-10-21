from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from conf.settings import EMAIL_HOST_USER
from users.forms import RegistrationForm, LoginForm
from users.token import account_activation_token
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site


class UserAccountView(TemplateView):
    template_name = 'registration/user-account.html'


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('users:login'))
    else:
        return render(request, 'email/email_not_verify.html')


def send_email_verification(request, user):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('users:verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_site.domain}{verification_url}"

    text_content = render_to_string(
        'email/verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject="Email Verification",
        body=text_content,
        from_email=EMAIL_HOST_USER,
        to=[user.email]
    )
    message.attach_alternative(text_content, "text/html")
    message.send()


class RegisterView(CreateView):
    template_name = 'registration/user-register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        send_email_verification(self.request, user)
        message = _('Registration was successfully registered')
        messages.success(self.request, message)
        return super().form_valid(form)


class LoginUserView(LoginView):
    template_name = 'registration/user-login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_page:home')


class UserResetPasswordView(TemplateView):
    template_name = 'registration/user-reset-password.html'
