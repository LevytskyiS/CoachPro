from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MealPlanPage(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.OneToOneField(
        User, related_name="mealplan_page", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Meal plan page of {self.user}"

    def get_absolute_url(self):
        return reverse("mealplan:mealplan_page_detail", kwargs={"pk": self.pk})


class Meal(models.Model):
    name = models.CharField(max_length=256)
    mealplan_page = models.ForeignKey(
        MealPlanPage, related_name="meal", on_delete=models.CASCADE
    )

    def get_proteins(self):
        meal_info_objs = [mi for mi in self.meal_info.all()]
        proteins = sum([mi_obj.food.proteins for mi_obj in meal_info_objs])
        return proteins

    def get_fats(self):
        meal_info_objs = [mi for mi in self.meal_info.all()]
        fats = sum([mi_obj.food.fats for mi_obj in meal_info_objs])
        return fats

    def get_carbohydrates(self):
        meal_info_objs = [mi for mi in self.meal_info.all()]
        carbohydrates = sum([mi_obj.food.carbohydrates for mi_obj in meal_info_objs])
        return carbohydrates

    def get_calories(self):
        meal_info_objs = [mi for mi in self.meal_info.all()]
        calories = sum([mi_obj.food.calories for mi_obj in meal_info_objs])
        return calories

    def __str__(self):
        return f"Meal '{self.name}' of {self.mealplan_page.user}"


class Food(models.Model):
    name = models.CharField(max_length=256)
    proteins = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    fats = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    carbohydrates = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    calories = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return self.name


class MealInfo(models.Model):
    meal = models.ForeignKey(Meal, related_name="meal_info", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="food_info", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("mealplan:mealplan_page_detail", kwargs={"pk": self.pk})
