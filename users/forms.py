from django.contrib.auth.forms import UserCreationForm

from catalog.forms import ValidationFormMixin
from users.models import User


class UserRegisterForm(ValidationFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['pass']
