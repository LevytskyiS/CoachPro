from django.urls import path

from . import views


app_name = "training"
urlpatterns = [
    # Training main page
    path(
        "<int:pk>/",
        views.TrainingPageDetailView.as_view(),
        name="training_page_detail",
    ),
    path(
        "create/<int:pk>/", views.CreateTrainingView.as_view(), name="create_training"
    ),
    path(
        "update/<int:pk>/", views.UpdateTrainingView.as_view(), name="update_training"
    ),
    path(
        "delete/<int:pk>/", views.DeleteTrainingView.as_view(), name="delete_training"
    ),
]
