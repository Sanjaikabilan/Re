from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class prop(models.Model):
    greet = models.TextField(max_length=500)
    
    def __unicode__(self):
        return self.greet

class orga(models.Model):
    ex = models.EmailField(max_length=254)
    
    def __unicode__(self):
        return self.ex
    
class orig(models.Model):
    secro = models.EmailField(max_length=254)
    
    def __unicode__(self):
        return self.secro

class Birth(models.Model):
    name = models.TextField(max_length=26)
    email = models.EmailField(max_length=143)
    team = models.TextField(max_length=26)
    bday = models.DateField()

    