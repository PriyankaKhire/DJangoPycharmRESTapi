from django.db import models

# Create your models here.
class Genere(models.Model):
    name = models.CharField(max_length=150)

    # This returns the string name
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    # This is a foreign key it's a one-to-many relationship
    genre = models.ForeignKey(Genere, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
