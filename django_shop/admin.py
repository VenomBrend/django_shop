from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User

from django_shop.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(auth_admin.UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
