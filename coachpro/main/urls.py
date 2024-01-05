from django.urls import path
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from . import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("clients", views.ClientListView.as_view(), name="client_list"),
    path(
        "progress/<int:pk>/",
        views.ClientDetailView.as_view(),
        name="client_detail",
    ),
    path(
        "clients/update/<int:pk>/",
        views.ClientUpdateView.as_view(),
        name="client_update",
    ),
    path("weight/", views.CreateWeight.as_view(), name="create_weight"),
    path("upload_file/", views.UploadFile.as_view(), name="upload_file"),
    path("upload_photo/", views.UploadPhoto.as_view(), name="upload_photo"),
    path("registration/", views.RegisterUser.as_view(), name="registration"),
    path("reset_password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "reset_password/done/",
        PasswordResetDoneView.as_view(template_name="main/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset_password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="main/password_reset_confirm.html",
            success_url="/reset_password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="main/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogOutUser.as_view(), name="logout"),
    path(
        "notepage/<int:pk>/",
        views.NotePageDetailView.as_view(),
        name="note_page_detail",
    ),
    path("note/<int:pk>/", views.CreateNoteView.as_view(), name="create_note"),
]
