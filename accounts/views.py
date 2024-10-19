from django.views.generic import TemplateView
from conf.settings import EMAIL_HOST_USER
# from users.form import LoginForm, RegistrationForm
from accounts.token import account_activation_token
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


class UserAccountView(TemplateView):
    template_name = 'registration/user-account.html'


class RegisterView(TemplateView):
    template_name = 'registration/user-register.html'


class LoginView(TemplateView):
    template_name = 'registration/user-login.html'


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
        return render(request, 'email_not_verify.html')


def send_email_verification(request, user):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('users:verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_site.domain}{verification_url}"

    text_content = render_to_string(
        'verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject="Verification Email",
        body=text_content,
        from_email=EMAIL_HOST_USER,
        to=[user.email]
    )
    message.attach_alternative(text_content, "text/html")
    message.send()
#
#
# # @method_decorator(csrf_protect, name='dispatch')
# @method_decorator(csrf_protect, name='dispatch')
# class RegisterView(TemplateView):
#     template_name = 'registration/user-register.html'

    # def post(self, request, *args, **kwargs):
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.set_password(form.cleaned_data['password1'])
    #         user.is_active = False
    #         user.save()
    #         send_email_verification(request, user)
    #         return redirect(reverse_lazy('users:login'))
    #     else:
    #         errors = form.errors
    #         return self.render_to_response({'errors': errors, 'form': form})
    #
    # def get(self, request, *args, **kwargs):
    #     form = RegistrationForm()
    #     return self.render_to_response({'form': form})
#
#
# class LoginView(TemplateView):
#     template_name = 'user-login.html'
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request=request, email=email, password=password)
#             if user is not None:
#                 login(user=user, request=request)
#                 return redirect(reverse_lazy('home_page:home'))
#             else:
#                 errors = form.errors
#                 return self.render_to_response({'errors': errors})
#         return self.render_to_response({})
#
#     def get(self, request, *args, **kwargs):
#         return self.render_to_response({})
#
#
# class LogoutView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('/')
