from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm
from users.models import User


class UserRegister(CreateView):
    model = User
    form_class = UserRegisterForm


class UserProfile(UpdateView):
    pass
