from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
    full_name = models.CharField(max_length=256)
    birthday = models.DateField(null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.full_name

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telephone = models.CharField(max_length=20)
    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
