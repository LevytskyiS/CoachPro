from django.forms import ModelForm, TextInput

from .models import TrainingDay


class CreateTrainingDayForm(ModelForm):
    class Meta:
        model = TrainingDay
        fields = ["day", "training"]
