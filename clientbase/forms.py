from django.contrib.auth.forms import UserCreationForm

from clientbase.models import CustomUser


class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")
