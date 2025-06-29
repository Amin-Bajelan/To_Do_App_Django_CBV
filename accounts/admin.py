from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["user", "first_name", "last_name"]
    list_filter = ['user', 'first_name', 'last_name']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)