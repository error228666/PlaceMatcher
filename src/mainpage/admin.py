from django.contrib import admin
from .models import Profile


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):  # StackedInline normally is used for formsets
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = (
    'username', 'email', 'first_name', 'last_name')  # Add Profile Fields to List View
    list_select_related = ('profile',)

    def get_inline_instances(self, request, obj=None):  # get_inline_instances display the inlines only in the edit form
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)