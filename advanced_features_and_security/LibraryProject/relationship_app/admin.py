from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Author, Book, Library, Librarian


# Register your models here.
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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)