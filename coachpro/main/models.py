from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    LIFESTYLE_CHOICES = {
        "A": "Active",
        "P": "Passive",
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_client = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    lifestyle = models.CharField(null=True, max_length=1, choices=LIFESTYLE_CHOICES)
    blood_pressure = models.IntegerField(null=True)
    chronic_illness = models.CharField(max_length=200)
    spine = models.CharField(max_length=200)
    schedule = models.TextField(max_length=1000)
    steps = models.IntegerField(null=True)
    muscles = models.CharField(max_length=200)
    unfavourite_food = models.CharField(max_length=200)
    food_allergies = models.CharField(max_length=200)
    favourite_food = models.CharField(max_length=200)
    test_results = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.user.username

    def get_absolute_url(self):
        return reverse("main:client_detail", kwargs={"pk": self.pk})

    def get_photos(self):
        return self.photos.all()

    def get_files(self):
        return self.files.all()

    def get_all_weights(self):
        return self.weights.all()


class Weight(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="weights", on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)


class Photo(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="photos", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="photo")

    def __str__(self) -> str:
        return str(self.image)


class File(models.Model):
    profile = models.ForeignKey(Profile, related_name="files", on_delete=models.CASCADE)
    file = models.FileField(upload_to="file")

    def __str__(self) -> str:
        return str(self.file)


class NotePage(models.Model):
    created_at = models.DateField(auto_now_add=True)
    profile = models.OneToOneField(
        Profile, related_name="notepage", on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse("main:note_page_detail", kwargs={"pk": self.pk})

    def get_all_notes(self):
        return self.notes.all()


class Note(models.Model):
    user = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)
    note_page = models.ForeignKey(
        NotePage, related_name="notes", on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1000, editable=True)
