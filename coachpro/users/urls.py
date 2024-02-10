from django.urls import path
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

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
    path("reset_password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "reset_password/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset_password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url="/reset_password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
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
