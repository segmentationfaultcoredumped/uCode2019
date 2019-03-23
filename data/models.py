from django.db import models
import datetime

# Create your models here.


class Session(models.Model):
    BOOL_CHOICES = ((True, 'Natural'), (False, 'Artificial'))

    # General info
    name = models.CharField(max_length=64)
    training = models.TextField(max_length=500, blank=True)
    date = models.DateField(default=datetime.date.today)
    # Environment conditions
    grass = models.BooleanField(choices=BOOL_CHOICES, blank=True)
    wet = models.BooleanField(blank=True)
    temp = models.IntegerField(blank=True)
    hum = models.IntegerField(blank=True)
    additional_info = models.TextField(max_length=240, blank=True)
