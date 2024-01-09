from django.contrib import admin
from .models import Profile, PatientR, Room

# Register your models here.

admin.site.register(Profile)
admin.site.register(PatientR)
admin.site.register(Room)
