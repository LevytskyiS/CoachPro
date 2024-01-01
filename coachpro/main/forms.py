from django.forms import (
    ModelForm,
    CharField,
    EmailField,
    EmailInput,
    TextInput,
    PasswordInput,
    FileInput,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile, Weight, File


class RegisterUserForm(UserCreationForm):
    username = CharField(label="Login", widget=TextInput())
    email = EmailField(label="Email", widget=EmailInput())
    password1 = CharField(label="Password", widget=PasswordInput())
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = CharField(label="Login", widget=TextInput())
    password = CharField(label="Password", widget=PasswordInput())


class CreateWeightForm(ModelForm):
    class Meta:
        model = Weight
        fields = ["value"]
        widgets = {
            "message": TextInput(
                attrs={"class": "form-control", "placeholder": "Your current weight"}
            ),
        }


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        exclude = ["profile"]
        widgets = {
            "file": FileInput(
                attrs={"class": "form-control", "placeholder": "Upload File"}
            ),
        }
