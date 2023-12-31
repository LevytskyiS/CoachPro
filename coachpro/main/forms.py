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

from .models import Profile, Weight, File, Photo, Note


class RegisterUserForm(UserCreationForm):
    first_name = CharField(label="First Name", widget=TextInput())
    last_name = CharField(label="Last Name", widget=TextInput())
    username = CharField(label="Login", widget=TextInput())
    email = EmailField(label="Email", widget=EmailInput())
    password1 = CharField(label="Password", widget=PasswordInput())
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class LoginUserForm(AuthenticationForm):
    username = CharField(label="Login", widget=TextInput())
    password = CharField(label="Password", widget=PasswordInput())


class CreateWeightForm(ModelForm):
    class Meta:
        model = Weight
        fields = ["value", "sleep_quality", "mood"]
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


class UploadPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ["profile"]
        # widgets = {"image": ImageField()}
        # fields = "__all__"
        image = ImageField()


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["text"]
        widgets = {
            "message": TextInput(
                attrs={"class": "form-control", "placeholder": "Note..."}
            ),
        }
