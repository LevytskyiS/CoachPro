from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
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
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Report, Photo, File
from .forms import CreateReporttForm, UploadPhotoForm, UploadFileForm


# Report sectiion
class CreateReportView(CreateView):
    model = Report
    form_class = CreateReporttForm
    request = HttpRequest()

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        form.instance.user = user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.user.profile.get_absolute_url_client()


class UpdateReportView(UpdateView):
    model = Report
    fields = [
        "weight",
        "sleep_quality",
        "mood",
    ]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.user.profile.get_absolute_url_client()


class DeleteReportView(DeleteView):
    model = Report
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.user.profile.get_absolute_url_client()


# Photo section
class UploadPhoto(FormView):
    form_class = UploadPhotoForm
    template_name = "users/client_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        user = User.objects.get(id=request.user.id)
        form.instance.user = user

        if form.is_valid():
            file = form.save()
            file.save()
            return HttpResponseRedirect(user.profile.get_absolute_url_client())


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.user.profile.get_absolute_url_client()


# File section
class UploadFile(FormView):
    form_class = UploadFileForm
    template_name = "users/client_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        print(request.user.id)
        user = User.objects.get(id=request.user.id)
        form.instance.user = user

        if form.is_valid():
            file = form.save()
            file.save()
            return HttpResponseRedirect(user.profile.get_absolute_url_client())


class FileDeleteView(DeleteView):
    model = File
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.user.profile.get_absolute_url_client()
