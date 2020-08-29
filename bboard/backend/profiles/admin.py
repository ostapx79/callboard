from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профель пользователя"""

    list_display = ("user", "email_two", "first_name")
