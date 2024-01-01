from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    LogoutView,
    PasswordResetConfirmView,
)
from django.http import HttpRequest, HttpResponseRedirect

from .models import Profile, Weight, File, Photo
from .forms import (
    RegisterUserForm,
    LoginUserForm,
    CreateWeightForm,
    UploadFileForm,
    UploadPhotoForm,
)


# Create your views here.
# class HomeDetailView(DetailView):
#     model = HomePageArticle
#     template_name = "main/index.html"
#     context_object_name = "article"


def index(request):
    return render(request, "main/index.html")


class ClientListView(ListView):
    model = Profile
    template_name = "main/client_list.html"
    context_object_name = "profiles"

    def get_queryset(self) -> QuerySet[Any]:
        return (
            # Фильтруемся по Profile
            Profile.objects.filter(is_client=True)
            # Фильтруемся по полю Profile.user (которое имеет ключ и связано с User) и его свойству User.is_active
            .filter(user__is_active=True)
        )


class ClientDetailView(DetailView):
    model = Profile
    template_name = "main/client_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateWeightForm()
        context["upload_file_form"] = UploadFileForm()
        context["upload_photo_form"] = UploadPhotoForm()
        return context

    # def post(self, request, *args, **kwars):
    #     form = CreateWeight(request.POST)
    #     print(form)


class CreateWeight(CreateView):
    model = Weight
    form_class = CreateWeightForm
    request = HttpRequest()

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs.get("pk")
        profile = Profile.objects.get(user=self.request.user.id)
        form.instance.profile = profile
        print(form.instance)
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.profile.get_absolute_url()


# def upload_file(request):
#     if request.method == "POST":
#         form = UploadFileForm(
#             request.POST,
#             request.FILES,
#         )
#         profile = Profile.objects.get(user=request.user.id)
#         form.instance.profile = profile
#         if form.is_valid():
#             file = form.save()
#             file.save()
#             return HttpResponseRedirect(profile.get_absolute_url())
#     else:
#         form = UploadFileForm()
#     return render(request, "main/client_detail.html", {"form": form})


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


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "main/registration.html"
    success_url = reverse_lazy("main:index")

    def form_valid(self, form):
        user = form.save()
        profile = Profile(user=user, is_client=True)
        profile.save()
        # login(self.request, user)
        return redirect("/")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"


class LogOutUser(LogoutView):
    # Logging out via GET requests to the built-in logout view is deprecated. Use POST requests instead.
    next_page = "/"
