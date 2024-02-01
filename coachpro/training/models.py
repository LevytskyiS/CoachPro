from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TrainingPage(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.OneToOneField(
        User, related_name="training_pages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Training page for {self.user}"

    def get_absolute_url(self):
        return reverse("training:training_page_detail", kwargs={"pk": self.pk})


class Training(models.Model):
    exercise = models.CharField(max_length=256)

    def __str__(self):
        return self.exercise


class TrainingDay(models.Model):
    training_page = models.ForeignKey(
        TrainingPage, related_name="training_days", on_delete=models.CASCADE
    )
    day = models.CharField(max_length=256)
    training = models.ManyToManyField(Training)

    def __str__(self):
        return f"Training day of {self.training_page.user}"
