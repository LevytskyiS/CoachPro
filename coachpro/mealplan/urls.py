from django.urls import path

from . import views

app_name = "mealplan"
urlpatterns = [
    # MealPlanPage and Meal Models create, update, delete
    path(
        "mealplan/<int:pk>/",
        views.MealPlanPageDetailView.as_view(),
        name="mealplan_page_detail",
    ),
    path("meal/<int:pk>/", views.CreateMealView.as_view(), name="create_meal"),
    path("meal/update/<int:pk>/", views.UpdateMealView.as_view(), name="update_meal"),
    path("meal/delete/<int:pk>/", views.DeleteMealView.as_view(), name="delete_meal"),
    # Meal info
    path(
        "create_meal_info/<int:pk>/",
        views.CreateMealInfoView.as_view(),
        name="create_meal_info",
    ),
    path(
        "update_meal_info/<int:pk>/",
        views.UpdateMealInfoView.as_view(),
        name="update_meal_info",
    ),
    path(
        "delete_meal_info/<int:pk>/",
        views.DeleteMealInfoView.as_view(),
        name="delete_meal_info",
    ),
]
