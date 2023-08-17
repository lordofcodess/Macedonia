from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
