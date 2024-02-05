from pprint import pprint

from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.http import HttpRequest
from django.contrib.auth.models import User

from .models import MealPlanPage, MealInfo, Meal, Food
from .forms import CreateMealForm, CreateMealInfoForm


# Training page
class MealPlanPageDetailView(DetailView):
    model = MealPlanPage
    template_name = "mealplan/mealplan_page_detail.html"
    context_object_name = "mealplan_page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["create_meal_form"] = CreateMealForm()
        context["create_meal_info_form"] = CreateMealInfoForm()
        return context


# Training day
class CreateMealView(CreateView):
    model = Meal
    form_class = CreateMealForm
    request = HttpRequest()

    def form_valid(self, form):
        mealplan_page = MealPlanPage.objects.get(id=self.kwargs.get("pk"))
        form.instance.mealplan_page = mealplan_page
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.mealplan_page.get_absolute_url()


class UpdateMealView(UpdateView):
    model = Meal
    context_object_name = "meal"
    fields = ["name"]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.mealplan_page.get_absolute_url()


class DeleteMealView(DeleteView):
    model = Meal
    context_object_name = "meal"
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.mealplan_page.get_absolute_url()


# Meal info
class CreateMealInfoView(CreateView):
    model = MealInfo
    form_class = CreateMealInfoForm
    request = HttpRequest()

    def form_valid(self, form):
        meal = Meal.objects.get(id=self.kwargs.get("pk"))
        form.instance.meal = meal
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.meal.mealplan_page.get_absolute_url()


class UpdateMealInfoView(UpdateView):
    model = MealInfo
    context_object_name = "mealinfo"
    fields = ["food"]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.meal.mealplan_page.get_absolute_url()


class DeleteMealInfoView(DeleteView):
    model = MealInfo
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.meal.mealplan_page.get_absolute_url()
