from django.forms import (
    ModelForm,
    CharField,
    EmailField,
    EmailInput,
    TextInput,
    PasswordInput,
    FileInput,
    ImageField,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class LoginUserForm(AuthenticationForm):
    username = CharField(label="Login", widget=TextInput())
    password = CharField(label="Password", widget=PasswordInput())


class UpdateUserProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user", "is_client", "is_coach", "coach", "clients"]
