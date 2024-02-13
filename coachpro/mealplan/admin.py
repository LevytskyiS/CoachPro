from django.contrib import admin
from .models import MealPlanPage, Meal, Food, MealInfo

admin.site.register(MealPlanPage)
admin.site.register(Meal)
admin.site.register(MealInfo)
admin.site.register(Food)
