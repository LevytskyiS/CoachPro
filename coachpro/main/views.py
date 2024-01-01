from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login

from .models import Profile
from .forms import RegisterUserForm


# Create your views here.
# class HomeDetailView(DetailView):
#     model = HomePageArticle
#     template_name = "main/index.html"
#     context_object_name = "article"


def index(request):
    return render(request, "main/index.html")


class ClientListView(ListView):
    model = Profile
    template_name = "main/client_list.html"
    context_object_name = "profiles"

    def get_queryset(self) -> QuerySet[Any]:
        return (
            # Фильтруемся по Profile
            Profile.objects.filter(is_client=True)
            # Фильтруемся по полю Profile.user (которое имеет ключ и связано с User) и его свойству User.is_active
            .filter(user__is_active=True)
        )


class ClientDetailView(DetailView):
    model = Profile
    template_name = "main/client_detail.html"


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "main/registration.html"
    success_url = reverse_lazy("main:index")

    def form_valid(self, form):
        user = form.save()
        profile = Profile(user=user, is_client=True)
        profile.save()
        login(self.request, user)
        return redirect("/")
