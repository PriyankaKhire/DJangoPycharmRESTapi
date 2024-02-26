from django.db import models

# Create your models here.
class Player(models.Model):
    playerId = models.CharField(max_length=100)
    playerBirthYear = models.CharField(max_length=100)
    playerBirthMonth = models.CharField(max_length=100)
    playerBirthDay = models.CharField(max_length=100)
    birthCountry = models.CharField(max_length=100)
    birthState = models.CharField(max_length=100)
    birthCity = models.CharField(max_length=100)
    playerDeathYear = models.CharField(max_length=100)
    playerDeathMonth = models.CharField(max_length=100)
    playerDeathDay = models.CharField(max_length=100)
    deathCountry = models.CharField(max_length=100)
    deathState = models.CharField(max_length=100)
    deathCity = models.CharField(max_length=100)
    nameFirst = models.CharField(max_length=50)
    nameLast = models.CharField(max_length=50)
    nameGiven = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    bats = models.CharField(max_length=1)
    throws = models.CharField(max_length=1)
    # Don't want to mess with date field for now
    debut = models.CharField(max_length=100)
    finalGame = models.CharField(max_length=100)
    retroID = models.CharField(max_length=100)
    bbrefID = models.CharField(max_length=100)
