from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профель пользователя"""

    list_display = (
        "user",
        "first_name",
        "last_name",
        "phone",
        "email_two",
        "id"
    )
    search_fields = (
        "user",
        "first_name",
        "last_name",
        "phone",
        "email_two"
    )
