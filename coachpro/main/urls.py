from django.urls import path

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
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogOutUser.as_view(), name="logout"),
    path(
        "notepage/<int:pk>/",
        views.NotePageDetailView.as_view(),
        name="note_page_detail",
    ),
    path("note/<int:pk>/", views.CreateNoteView.as_view(), name="create_note"),
]
