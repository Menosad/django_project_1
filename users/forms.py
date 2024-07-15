from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from catalog.forms import ValidationFormMixin
from users.models import User


class UserRegisterForm(ValidationFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'nick_name', 'country', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
