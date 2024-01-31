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

from .models import TrainingPage, TrainingDay, Training, TrainingStats
from .forms import CreateTrainingDayForm, CreateTrainingStatsForm


# Training page
class TrainingPageDetailView(DetailView):
    model = TrainingPage
    template_name = "training/training_page_detail.html"
    context_object_name = "training_page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_training_day"] = CreateTrainingDayForm()
        context["form_training_stats"] = CreateTrainingStatsForm()
        return context


# Training stats
class CreateTrainingStatsView(CreateView):
    model = TrainingStats
    form_class = CreateTrainingStatsForm
    request = HttpRequest()

    def form_valid(self, form):
        training = Training.objects.get(id=self.kwargs.get("pk"))
        form.instance.training = training
        # user = User.objects.get(id=training_page.user.id)
        # form.instance.user = user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.request.META["HTTP_REFERER"]


class CreateTrainingDayView(CreateView):
    model = TrainingDay
    form_class = CreateTrainingDayForm
    request = HttpRequest()

    def form_valid(self, form):
        training_page = TrainingPage.objects.get(id=self.kwargs.get("pk"))
        form.instance.training_page = training_page
        user = User.objects.get(id=training_page.user.id)
        form.instance.user = user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


class UpdateTrainingDayView(UpdateView):
    model = TrainingDay
    context_object_name = "training_day"
    fields = [
        "training",
    ]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


class DeleteTrainingDayView(DeleteView):
    model = TrainingDay
    context_object_name = "training_day"
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()
