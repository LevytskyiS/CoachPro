from django.forms import ModelForm, TextInput

from .models import Meal, MealInfo


class CreateMealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ["name"]


class CreateMealInfoForm(ModelForm):
    class Meta:
        model = MealInfo
        exclude = ["meal"]