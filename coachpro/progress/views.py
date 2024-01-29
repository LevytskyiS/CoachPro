from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    FormView,
    UpdateView,
    DeleteView,
)
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from .models import Report, Photo, File
from .forms import CreateReporttForm, UploadPhotoForm, UploadFileForm


# Report sectiion
class ReportListView(ListView):
    model = Report


# Photo section
class UploadPhoto(FormView):
    form_class = UploadPhotoForm
    template_name = "users/client_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        user = User.objects.get(user=request.user.id)
        form.instance.user = user

        if form.is_valid():
            file = form.save()
            file.save()
            return HttpResponseRedirect(user.profile.get_absolute_url_client())


# File section
class UploadFile(FormView):
    form_class = UploadFileForm
    template_name = "users/client_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        user = User.objects.get(user=request.user.id)
        form.instance.user = user

        if form.is_valid():
            file = form.save()
            file.save()
            return HttpResponseRedirect(user.profile.get_absolute_url_client())
