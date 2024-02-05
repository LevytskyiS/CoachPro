from django.forms import ModelForm, TextInput
from .models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["text"]
        widgets = {
            "message": TextInput(
                attrs={"class": "form-control", "placeholder": "Note..."}
            ),
        }
