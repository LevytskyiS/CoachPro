from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    FormView,
    UpdateView,
    DeleteView,
)


def index(request):
    return render(request, "users/index.html")


# Clients section
class ClientListView(ListView):
    model = User
    template_name = "users/client_list.html"
    context_object_name = "users"
    paginate_by = 5

    def get_queryset(self):
        users = User.objects.filter(is_active=True).filter(profile__is_client=True)
        return users


class ClientDetailView(DetailView):
    model = User
    template_name = "users/client_detail.html"


# Coach section
class TrainerListView(ListView):
    model = User
    template_name = "users/trainer_list.html"
    context_object_name = "trainers"
    paginate_by = 5

    def get_queryset(self):
        trainers = User.objects.filter(is_active=True).filter(profile__is_coach=True)
        return trainers


class TrainerDetailView(DetailView):
    model = User
    template_name = "users/trainer_detail.html"
    context_object_name = "trainer"
