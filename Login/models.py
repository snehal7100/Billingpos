from django.db import models

# Create your models here.
class MLogin(models.Model):
    email = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)
   