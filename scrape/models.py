from django.db import models

# Create your models here.

class Website(models.Model):
    link = models.CharField(max_length=1000)