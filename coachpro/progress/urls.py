from django.urls import path

from . import views

app_name = "progress"
urlpatterns = [
    path("report/", views.ReportListView.as_view(), name="report_list"),
]
