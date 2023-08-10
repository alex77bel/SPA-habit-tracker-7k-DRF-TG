from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_editable = ('email', 'is_active', 'is_staff', 'is_superuser')