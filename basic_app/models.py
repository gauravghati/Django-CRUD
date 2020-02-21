from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Questions(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
    accuracy = models.IntegerField(default=0)

    def __str__(self):
        return self.title
