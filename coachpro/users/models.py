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
    coach = models.ManyToManyField(User, related_name="coach", blank=True, null=True)
    clients = models.ManyToManyField(
        User, related_name="clients", blank=True, null=True
    )
    age = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    lifestyle = models.CharField(
        max_length=7, choices=LIFESTYLE_CHOICES, blank=True, null=True
    )
    blood_pressure = models.IntegerField(blank=True, null=True)
    chronic_illness = models.CharField(max_length=200, blank=True, null=True)
    spine = models.CharField(max_length=200, blank=True, null=True)
    schedule = models.TextField(max_length=1000, blank=True, null=True)
    steps = models.IntegerField(null=True, blank=True)
    muscles = models.CharField(max_length=200, blank=True, null=True)
    unfavourite_food = models.CharField(max_length=200, blank=True, null=True)
    food_allergies = models.CharField(max_length=200, blank=True, null=True)
    favourite_food = models.CharField(max_length=200, blank=True, null=True)
    test_results = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.user.username + "'s profile"
