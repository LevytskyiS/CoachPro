from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpRequest

from .models import Note, NotePage
from .forms import CreateNoteForm


# NotePage and Note objects create, update, delete
class NotePageDetailView(DetailView):
    model = NotePage
    template_name = "notes/note_page_detail.html"
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
