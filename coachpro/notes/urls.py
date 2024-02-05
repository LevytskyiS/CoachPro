from django.urls import path

from . import views

app_name = "notes"
urlpatterns = [
    # Notepage and Note Models create, update, delete
    path(
        "notepage/<int:pk>/",
        views.NotePageDetailView.as_view(),
        name="note_page_detail",
    ),
    path("note/<int:pk>/", views.CreateNoteView.as_view(), name="create_note"),
    path("note/update/<int:pk>/", views.UpdateNoteView.as_view(), name="update_note"),
    path("note/delete/<int:pk>/", views.DeleteNoteView.as_view(), name="delete_note"),
]
