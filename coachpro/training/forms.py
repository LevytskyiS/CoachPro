from django.forms import ModelForm, TextInput

from .models import Training


class CreateTrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ["text"]
        widgets = {
            "message": TextInput(
                attrs={"class": "form-control", "placeholder": "Training"}
            ),
        }
