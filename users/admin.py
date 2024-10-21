from django.contrib import admin

from users.models import UserModel


@admin.register(UserModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'date_joined',)
    ordering = ('-date_joined',)
