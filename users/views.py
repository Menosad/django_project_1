import secrets

from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class UserRegister(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy(f'users:verification_message')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            token = secrets.token_hex(16)
            user.is_active = False
            user.token = token
            user.save()
            host = self.request.get_host()
            url = f"http://{host}/users/email-confirm/{token}/"
            send_mail(
                subject='Подтверждение почты',
                message=f"Вы прошли регистрацию на сайте. Для подтверждения почты пожалуйста прейдите\n"
                        f"по ссылке: {url}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
        return super().form_valid(form)


def verification(request):
    context = {
        'message': f'На  почту указанную при регистрации отправлено письмо, пройдите по ссылке'
                   f'для завершения регистрации'
    }
    return render(request, 'users/verification_message.html', context)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:users_login'))


class UserProfile(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:user_profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetail(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


def recover_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=['password'])
        send_mail(
             'Смена пароля',
             f'Ваш новый пароль: {password}',
             EMAIL_HOST_USER,
             [user.email],
        )
        return redirect(reverse_lazy('users:users_login'))
    return render(request, 'users/recover_password.html')
