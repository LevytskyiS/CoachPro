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

from .models import TrainingPage, TrainingDay, Training, TrainingStats, TrainingInfo
from .forms import (
    CreateTrainingDayForm,
    UpdateTrainingStats,
    CreateTrainingStatsForm,
    CreateTrainingInfoForm,
)


# Training page
class TrainingPageDetailView(DetailView):
    model = TrainingPage
    template_name = "training/training_page_detail.html"
    context_object_name = "training_page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_training_day"] = CreateTrainingDayForm()
        context["create_training_info_form"] = CreateTrainingInfoForm()
        context["create_training_stats_form"] = CreateTrainingStatsForm()
        context["update_training_stats_form"] = UpdateTrainingStats()
        return context


# Training day
class CreateTrainingDayView(CreateView):
    model = TrainingDay
    form_class = CreateTrainingDayForm
    request = HttpRequest()

    def form_valid(self, form):
        training_page = TrainingPage.objects.get(id=self.kwargs.get("pk"))
        form.instance.training_page = training_page
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


class UpdateTrainingDayView(UpdateView):
    model = TrainingDay
    context_object_name = "training_day"
    fields = ["day"]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


class DeleteTrainingDayView(DeleteView):
    model = TrainingDay
    context_object_name = "training_day"
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


# Training info
class CreateTrainingInfoView(CreateView):
    model = TrainingInfo
    form_class = CreateTrainingInfoForm
    request = HttpRequest()

    def form_valid(self, form):
        training_day = TrainingDay.objects.get(id=self.kwargs.get("pk"))
        form.instance.training_day = training_day
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.training_day.training_page.get_absolute_url()


class DeleteTrainingInfoView(DeleteView):
    model = TrainingInfo
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.training_day.training_page.get_absolute_url()


# Training stats
class CreateTrainingStatsView(CreateView):
    model = TrainingStats
    form_class = CreateTrainingStatsForm
    request = HttpRequest()

    def form_valid(self, form):
        training_page = TrainingInfo.objects.get(id=self.kwargs.get("pk"))
        form.instance.training_info = training_page
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.training_info.training_day.training_page.get_absolute_url()


class UpdateTrainingStatsView(UpdateView):
    model = TrainingStats
    context_object_name = "training_stats"
    fields = ["weight", "reps", "sets"]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        training_info = TrainingInfo.objects.get(training_stats=self.kwargs.get("pk"))
        training_day = TrainingDay.objects.get(workout_info=training_info)
        return training_day.training_page.get_absolute_url()


class DeleteTrainingStatsView(DeleteView):
    model = TrainingStats
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        training_info = TrainingInfo.objects.get(training_stats=self.kwargs.get("pk"))
        training_day = TrainingDay.objects.get(workout_info=training_info)
        return training_day.training_page.get_absolute_url()
