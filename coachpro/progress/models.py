from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Report(models.Model):
    SLEEP_QUALITY_CHOICES = {
        "1": "Really bad",
        "2": "Bad",
        "3": "Ok",
        "4": "Good",
        "5": "Perfect",
    }
    MOOD_CHOICES = {
        "1": "Really bad",
        "2": "Bad",
        "3": "Ok",
        "4": "Good",
        "5": "Perfect",
    }

    user = models.ForeignKey(User, related_name="reports", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sleep_quality = models.CharField(
        blank=True, null=True, max_length=10, choices=SLEEP_QUALITY_CHOICES
    )
    mood = models.CharField(blank=True, null=True, max_length=10, choices=MOOD_CHOICES)

    def get_absolute_url(self):
        return reverse("users:client_detail", kwargs={"pk": self.pk})


class Photo(models.Model):
    user = models.ForeignKey(User, related_name="photo", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photo")

    def str(self) -> str:
        return str(self.image)

    def get_absolute_url(self):
        return reverse("users:client_detail", kwargs={"pk": self.pk})

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Photo, self).delete(*args, **kwargs)
        storage.delete(path)


class File(models.Model):
    user = models.ForeignKey(User, related_name="file", on_delete=models.CASCADE)
    file = models.FileField(upload_to="file")

    def str(self) -> str:
        return str(self.file)

    def get_absolute_url(self):
        return reverse("users:client_detail", kwargs={"pk": self.pk})

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path
        super(File, self).delete(*args, **kwargs)
        storage.delete(path)
