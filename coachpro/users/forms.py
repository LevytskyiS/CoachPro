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


class LoginUserForm(AuthenticationForm):
    username = CharField(label="Login", widget=TextInput())
    password = CharField(label="Password", widget=PasswordInput())
