from django.forms import ModelForm, TextInput

from .models import TrainingDay, TrainingInfo, TrainingStats


class CreateTrainingDayForm(ModelForm):
    class Meta:
        model = TrainingDay
        fields = ["day"]


class UpdateTrainingStats(ModelForm):
    class Meta:
        model = TrainingStats
        exclude = ["training_info"]


class CreateTrainingStatsForm(ModelForm):
    class Meta:
        model = TrainingStats
        exclude = ["training_info"]
