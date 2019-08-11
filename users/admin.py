from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mode',)}),
    )


admin.site.register(User, MyUserAdmin)
