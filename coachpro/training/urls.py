from django.urls import path

from . import views

app_name = "training"
urlpatterns = [
    path(
        "<int:pk>/",
        views.TrainingPageDetailView.as_view(),
        name="training_page_detail",
    ),
    # Training days
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
    # Training info
    path(
        "create_info/<int:pk>/",
        views.CreateTrainingInfoView.as_view(),
        name="create_training_info",
    ),
    path(
        "delete_info/<int:pk>/",
        views.DeleteTrainingInfoView.as_view(),
        name="delete_training_info",
    ),
    # Training stats
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
