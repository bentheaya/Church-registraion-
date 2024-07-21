from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Member

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )
    list_display = ('username', 'email', 'is_admin')
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'phone_number', 'email_address', 'membership_status')
    search_fields = ('full_name', 'email_address')

admin.site.register(CustomUser, CustomUserAdmin)
	