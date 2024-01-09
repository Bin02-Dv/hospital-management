from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class PatientR(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    marital = models.CharField(max_length=20)
    lga = models.CharField(max_length=100)
    addrss = models.TextField(blank=True)
    state = models.CharField(max_length=100)
    apparatus = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    code = models.CharField(max_length=1000)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.full_name

class Room(models.Model):
    room = models.CharField(max_length=100)
    room_discription = models.TextField(max_length=100)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.room
