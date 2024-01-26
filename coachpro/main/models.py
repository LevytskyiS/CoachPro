from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    LIFESTYLE_CHOICES = {
        "Active": "Active",
        "Passive": "Passive",
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_client = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    clients = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    lifestyle = models.CharField(null=True, max_length=7, choices=LIFESTYLE_CHOICES)
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

    def __str__(self):
        return self.user.username + "'s profile"
