from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    year_published = models.PositiveSmallIntegerField()