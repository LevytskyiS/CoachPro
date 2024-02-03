from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Login, registration, logout, password reset
    path("registration/", views.RegisterUser.as_view(), name="registration"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogOutUser.as_view(), name="logout"),
    path(
        "registration_confirmation/",
        views.registration_confirmation,
        name="registration_confirmation",
    ),
    # ...
    # List of clients
    path("clients/", views.ClientListView.as_view(), name="client_list"),
    # Client's profile
    path("profile/<int:pk>", views.ClientDetailView.as_view(), name="client_detail"),
    path(
        "profile_update/<int:pk>",
        views.UpdateUserProfileView.as_view(),
        name="profile_update",
    ),
    # List of trainers
    path("trainers/", views.TrainerListView.as_view(), name="trainer_list"),
    # Trainer's profile
    path("trainer/<int:pk>", views.TrainerDetailView.as_view(), name="trainer_detail"),
]
