from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegister, UserProfile, UserDetail

app_name = UsersConfig.name

urlpatterns = [
    path("users_login/", LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path("users_logout/", LogoutView.as_view(), name='users_logout'),
    path("users_register/", UserRegister.as_view(), name='users_register'),
    path("user_profile/", UserDetail.as_view(), name='user_profile'),
    path("user_edit/", UserProfile.as_view(), name='user_edit'),
]
