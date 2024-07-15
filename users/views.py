from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserRegister(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_profile')


class UserProfile(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:user_edit')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetail(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user
