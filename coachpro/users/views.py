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
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    LogoutView,
    PasswordResetConfirmView,
)

from .forms import LoginUserForm
from progress.forms import CreateReporttForm, UploadFileForm, UploadPhotoForm


def index(request):
    return render(request, "users/index.html")


# Log in
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"


# Log out
class LogOutUser(LogoutView):
    # Logging out via GET requests to the built-in logout view is deprecated. Use POST requests instead.
    next_page = "/"


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateReporttForm()
        context["upload_file_form"] = UploadFileForm()
        context["upload_photo_form"] = UploadPhotoForm()
        return context


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
