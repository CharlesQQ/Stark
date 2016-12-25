from django.db import models

# Create your models here.

class Host(models.Model):
    hostname=models.CharField(max_length=123,unique=True)

