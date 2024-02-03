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


class TrainingStats(models.Model):
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()


class TrainingDay(models.Model):
    day = models.CharField(max_length=256)
    training_page = models.ForeignKey(
        TrainingPage, related_name="training_day", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Training day '{self.day}' of {self.training_page.user}"


class TrainingInfo(models.Model):
    training = models.OneToOneField(
        Training, related_name="training_info", on_delete=models.CASCADE
    )
    stats = models.ForeignKey(
        TrainingStats, related_name="training_stats", on_delete=models.CASCADE
    )
    training_day = models.ForeignKey(
        TrainingDay, related_name="workout_info", on_delete=models.CASCADE
    )
