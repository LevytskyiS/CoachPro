from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Login, registration, logout, password reset
    # ...
    # List of clients
    path("clients/", views.ClientListView.as_view(), name="client_list"),
]
