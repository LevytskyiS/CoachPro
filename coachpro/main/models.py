from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_client = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


# class HomePageArticle(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField(max_length=1000)

#     def __str__(self) -> str:
#         return self.title
