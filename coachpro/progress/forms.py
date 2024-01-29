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

from .models import Report, Photo, File


class CreateReporttForm(ModelForm):
    class Meta:
        model = Report
        fields = ["weight", "sleep_quality", "mood"]
        # widgets = {
        #     "message": TextInput(
        #         attrs={"class": "form-control", "placeholder": "Your current weight"}
        #     ),
        # }


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        exclude = ["user"]
        # widgets = {
        #     "file": FileInput(
        #         attrs={"class": "form-control", "placeholder": "Upload File"}
        #     ),
        # }


class UploadPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ["user"]
        # widgets = {"image": ImageField()}
        # fields = "all"
        image = ImageField()
