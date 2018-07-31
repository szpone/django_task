from django.db import models
from random import randint
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    birthday = models.DateField(null=True)
    random_number = models.IntegerField(default=randint(1, 101))
