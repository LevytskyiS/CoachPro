from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class NotePage(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, related_name="notepage", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("notes:note_page_detail", kwargs={"pk": self.pk})

    def get_all_notes(self):
        return self.notes.all()


class Note(models.Model):
    user = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)
    note_page = models.ForeignKey(
        NotePage, related_name="notes", on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1000, editable=True)
    created_at = models.DateField(auto_now_add=True)
