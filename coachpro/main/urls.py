from django.urls import path

from . import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("clients", views.ClientListView.as_view(), name="client_list"),
    path(
        "clients/client/<int:pk>/",
        views.ClientDetailView.as_view(),
        name="client_detail",
    ),
]
