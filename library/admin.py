from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
	list_display = ('username', 'first_name', 'last_name', 'patronymic', 'phone_number')
	fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "patronymic", "email", "phone_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 
                       'password1', 
                       'password2', 
                       'is_staff', 
                       'is_active', 
                       'first_name', 
                       'last_name',
					   'patronymic',
					   'phone_number')}
        ),
    )

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 
					'author', 
					'annotation', 
					'publication_year', 
					'created_at']
	list_filter = ['name', 
                   'author', 
                   'annotation', 
                   'publication_year', 
                   'created_at']
	search_fields = ['name',]
	ordering = ['name',]
