from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.http import HttpRequest

from .models import TrainingPage, Training
from .forms import CreateTrainingForm
from main.models import Profile


# Create your views here.
class TrainingPageDetailView(DetailView):
    model = TrainingPage
    template_name = "training/training_page_detail.html"
    context_object_name = "trainingpage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateTrainingForm()
        return context


class CreateTrainingView(CreateView):
    model = Training
    form_class = CreateTrainingForm
    request = HttpRequest()

    def form_valid(self, form):
        training_page = TrainingPage.objects.get(id=self.kwargs.get("pk"))
        form.instance.training_page = training_page
        profile = Profile.objects.get(id=training_page.profile.id)
        form.instance.profile = profile
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


class UpdateTrainingView(UpdateView):
    model = Training
    fields = [
        "text",
    ]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()


class DeleteTrainingView(DeleteView):
    model = Training
    template_name_suffix = "_confirm_delete"

    def get_success_url(self) -> str:
        return self.object.training_page.get_absolute_url()
