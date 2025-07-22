from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book,CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add our custom fields to what's displayed in the admin "edit" page
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Add our custom fields to the admin "add" user page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "classes": ("wide",),
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    # Show these fields in the user list view
    list_display = ["username", "email", "first_name", "last_name", "date_of_birth", "is_staff"]


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
