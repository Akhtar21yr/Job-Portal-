from django.contrib import admin
from .models import User,UserProfile,UserEducation,UserSkill,UserPersonalInfo,UserExperince
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email", "name","tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []
@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ['skill','user_email']


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(UserProfile)
admin.site.register(UserEducation)
admin.site.register(UserPersonalInfo)
admin.site.register(UserExperince)
# admin.site.register(UserSkill)