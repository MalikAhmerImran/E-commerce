from django.contrib import admin
from djangoproject.accounts.models import User,Product,Order,OrderDetails,Images
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances
 

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id',"username", "email", "is_admin","is_verified",'is_owner']
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email",'password','is_active']}),
        ("Personal info", {"fields": ["username",'is_verified']}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)    
admin.site.register(Product)    
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Images)

