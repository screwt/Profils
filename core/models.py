from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Etat(models.Model):
    description=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.description} "

class Photo(models.Model):
    profil=models.ForeignKey("core.Profil",on_delete=models.CASCADE)
    path=models.ImageField()
    caption=models.CharField(max_length=200)

class Profil(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    date_de_naissance=models.DateField(auto_now=False, auto_now_add=False)
    classe=models.IntegerField()
    num_telephone=models.CharField(max_length=25)
    adresse=models.CharField(max_length=200)
    ville=models.CharField(max_length=50)
    situation=models.TextField()
    date_ajoute=models.DateTimeField(default=timezone.now)
    etat=models.ForeignKey("core.Etat",on_delete=models.SET_NULL,null=True)
    nomparrain = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"