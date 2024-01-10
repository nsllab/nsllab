from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, Bio

class MemberAdmin(UserAdmin):
    # Define your custom configurations for the Member model admin here
    list_display = ('username', 'password', 'email', 'address', 'login_cnt', 'last_login', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        # Include your custom fields in the fieldsets as needed
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'address', 'login_cnt')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Unregister the default User model
# admin.site.unregister(Member)

# Register your custom Member model with the custom admin class
admin.site.register(Member, MemberAdmin)
admin.site.register(Bio)
