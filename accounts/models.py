from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    userID = models.CharField(max_length=10)

