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
    return render(request, "main/index.html")


# Clients section
class ClientListView(ListView):
    model = User
    template_name = "main/client_list.html"
    context_object_name = "users"
    paginate_by = 10

    def get_queryset(self):
        return User.objects.filter(profile__is_client=True).filter(is_active=True)
