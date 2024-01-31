from django.forms import ModelForm, TextInput

from .models import TrainingDay, TrainingStats


class CreateTrainingDayForm(ModelForm):
    class Meta:
        model = TrainingDay
        fields = ["training"]


class CreateTrainingStatsForm(ModelForm):
    class Meta:
        model = TrainingStats
        exclude = ["training"]
