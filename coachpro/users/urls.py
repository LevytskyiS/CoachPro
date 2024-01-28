from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Login, registration, logout, password reset
    # ...
    # List of clients
    path("clients/", views.ClientListView.as_view(), name="client_list"),
    # Client's profile
    path("profile/<int:pk>", views.ClientDetailView.as_view(), name="client_detail"),
    # List of trainers
    path("trainers/", views.TrainerListView.as_view(), name="trainer_list"),
    # Trainer's profile
    path("trainer/<int:pk>", views.TrainerDetailView.as_view(), name="trainer_detail"),
]
