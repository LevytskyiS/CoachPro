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

    def __str__(self):
        return f"Meal '{self.name}' of {self.mealplan_page.user}"


class Food(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class MealInfo(models.Model):
    meal = models.ForeignKey(Meal, related_name="meal_info", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="food_info", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("mealplan:mealplan_page_detail", kwargs={"pk": self.pk})
