from django.urls import path

from . import views

app_name = "progress"
urlpatterns = [
    path("report/", views.CreateReportView.as_view(), name="create_report"),
    path(
        "report/update/<int:pk>/",
        views.UpdateReportView.as_view(),
        name="update_report",
    ),
    path(
        "report/delete/<int:pk>/",
        views.DeleteReportView.as_view(),
        name="delete_report",
    ),
    path("upload_file/", views.UploadFile.as_view(), name="upload_file"),
    path("upload_photo/", views.UploadPhoto.as_view(), name="upload_photo"),
    path("delete_file/<int:pk>/", views.FileDeleteView.as_view(), name="delete_file"),
    path(
        "delete_photo/<int:pk>/", views.PhotoDeleteView.as_view(), name="delete_photo"
    ),
]
