from django.urls import path

from . import views

app_name = "training"
urlpatterns = [
    path(
        "<int:pk>/",
        views.TrainingPageDetailView.as_view(),
        name="training_page_detail",
    ),
    path(
        "create/<int:pk>/",
        views.CreateTrainingDayView.as_view(),
        name="create_training_day",
    ),
    path(
        "update/<int:pk>/",
        views.UpdateTrainingDayView.as_view(),
        name="update_training_day",
    ),
    path(
        "delete/<int:pk>/",
        views.DeleteTrainingDayView.as_view(),
        name="delete_training_day",
    ),
    path(
        "create_stats/<int:pk>/",
        views.CreateTrainingStatsView.as_view(),
        name="create_training_stats",
    ),
    path(
        "update_stats/<int:pk>/",
        views.UpdateTrainingStatsView.as_view(),
        name="update_training_stats",
    ),
    path(
        "delete_stats/<int:pk>/",
        views.DeleteTrainingStatsView.as_view(),
        name="delete_training_stats",
    ),
]
