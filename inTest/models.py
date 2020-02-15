from django.db import models

# Create your models here.

class Mark(models.Model):
    name = models.CharField(max_length=20)
    mark = models.IntegerField()

