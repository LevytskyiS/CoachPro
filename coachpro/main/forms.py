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

from .models import Profile, Weight, File, Photo


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


# class CreateNoteForm(ModelForm):
#     class Meta:
#         model = Note
#         fields = ["text"]
#         widgets = {
#             "message": TextInput(attrs={"class": "form-control"}),
#         }


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        exclude = ["profile"]
        widgets = {
            "file": FileInput(
                attrs={"class": "form-control", "placeholder": "Upload File"}
            ),
        }


class UploadPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ["profile"]
        # widgets = {"image": ImageField()}
        # fields = "__all__"
        image = ImageField()
