from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from main.models import Profile


# Create your models here.
# class TrainingPage(models.Model):
#     created_at = models.DateField(auto_now_add=True)
#     profile = models.OneToOneField(
#         Profile, related_name="trainingpage", on_delete=models.CASCADE
#     )

#     def get_absolute_url(self):
#         return reverse("main:training_page_detail", kwargs={"pk": self.pk})

#     def get_all_trainingdays(self):
#         return self.trainingdays.all()


# class TrainingDay(models.Model):
#     profile = models.ForeignKey(
#         Profile, related_name="trainingdays", on_delete=models.CASCADE
#     )
#     training_page = models.ForeignKey(
#         TrainingPage, related_name="notes", on_delete=models.CASCADE
#     )
#     text = models.TextField(max_length=1000, editable=True)

#     def get_all_trainingdays(self):
#         return self.trainings.all()


# class Training(models.Model):
#     profile = models.ForeignKey(
#         Profile, related_name="trainings", on_delete=models.CASCADE
#     )
#     training_day = models.ForeignKey(
#         TrainingDay, related_name="training", on_delete=models.CASCADE
#     )
#     text = models.TextField(max_length=1000, editable=True)


class TrainingPage(models.Model):
    created_at = models.DateField(auto_now_add=True)
    profile = models.OneToOneField(
        Profile, related_name="trainingpage", on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse("training:training_page_detail", kwargs={"pk": self.pk})

    def get_training(self):
        return self.training


class Training(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="trainings", on_delete=models.CASCADE
    )
    training_page = models.OneToOneField(
        TrainingPage, related_name="training", on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1000, editable=True)
