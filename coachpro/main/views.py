from typing import Any
from django.contrib import messages
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    FormView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import logout, login
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    LogoutView,
    PasswordResetConfirmView,
)
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages.views import SuccessMessageMixin

from .models import Profile, Weight, File, Photo, Note, NotePage
from .forms import (
    RegisterUserForm,
    LoginUserForm,
    CreateWeightForm,
    UploadFileForm,
    UploadPhotoForm,
    CreateNoteForm,
)
from training.models import TrainingPage


def index(request):
    return render(request, "main/index.html")


class ClientListView(ListView):
    model = Profile
    template_name = "main/client_list.html"
    context_object_name = "profiles"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return Profile.objects.filter(is_client=True).filter(user__is_active=True)


# Client profile updates (profile data, uploading/removing photos and files)
class ClientDetailView(DetailView):
    model = Profile
    template_name = "main/client_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateWeightForm()
        context["upload_file_form"] = UploadFileForm()
        context["upload_photo_form"] = UploadPhotoForm()
        return context


class ClientUpdateView(UpdateView):
    model = Profile
    fields = [
        "age",
        "weight",
        "height",
        "lifestyle",
        "blood_pressure",
        "chronic_illness",
        "spine",
        "schedule",
        "muscles",
        "unfavourite_food",
        "food_allergies",
        "favourite_food",
        "test_results",
    ]
    template_name_suffix = "_update_form"


class UploadFile(FormView):
    form_class = UploadFileForm
    template_name = "main/client_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        profile = Profile.objects.get(user=request.user.id)
        form.instance.profile = profile

        if form.is_valid():
            file = form.save()
            file.save()
            return HttpResponseRedirect(profile.get_absolute_url())


class UploadPhoto(FormView):
    form_class = UploadPhotoForm
    template_name = "main/client_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        profile = Profile.objects.get(user=request.user.id)
        form.instance.profile = profile

        if form.is_valid():
            file = form.save()
            file.save()
            return HttpResponseRedirect(profile.get_absolute_url())


# Weight objects creating, updating, deleting
class CreateWeight(CreateView):
    model = Weight
    form_class = CreateWeightForm
    request = HttpRequest()

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs.get("pk")
        profile = Profile.objects.get(user=self.request.user.id)
        form.instance.profile = profile
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.profile.get_absolute_url()


class UpdateWeightView(UpdateView):
    model = Weight
    fields = [
        "value",
        "sleep_quality",
        "mood",
    ]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.profile.get_absolute_url()


class DeleteWeightView(DeleteView):
    model = Weight
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.profile.get_absolute_url()


# User registraiotn, login, logout, password reset
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "main/registration.html"
    success_url = reverse_lazy("main:index")

    def form_valid(self, form):
        user = form.save()
        profile = Profile(user=user, is_client=True)
        profile.save()
        note_page = NotePage(profile=profile)
        note_page.save()
        training_page = TrainingPage(profile=profile)
        training_page.save()
        login(self.request, user)
        return redirect("main:client_update", user.profile.id)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"


class LogOutUser(LogoutView):
    # Logging out via GET requests to the built-in logout view is deprecated. Use POST requests instead.
    next_page = "/"


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "main/password_reset.html"
    email_template_name = "main/password_reset_email.html"
    html_email_template_name = "main/password_reset_email.html"
    success_url = reverse_lazy("main:password_reset_done")
    success_message = (
        "An email with instructions to reset your password has been sent to %(email)s."
    )
    subject_template_name = "main/password_reset_subject.txt"


# NotePage and Note objects create, update, delete
class NotePageDetailView(DetailView):
    model = NotePage
    template_name = "main/note_page_detail.html"
    context_object_name = "notepage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateNoteForm()
        return context


class CreateNoteView(CreateView):
    model = Note
    form_class = CreateNoteForm
    request = HttpRequest()

    def form_valid(self, form):
        form.instance.note_page = NotePage.objects.get(id=self.kwargs.get("pk"))
        user = User.objects.get(id=self.request.user.id)
        form.instance.user = user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.note_page.get_absolute_url()


class UpdateNoteView(UpdateView):
    model = Note
    fields = [
        "text",
    ]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.note_page.get_absolute_url()


class DeleteNoteView(DeleteView):
    model = Note
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.note_page.get_absolute_url()
