from django.db import models

# Create your models here. every model gets a column called PK automatically made by Django, ID is an alias

# create a model for the places we want to visit, with a name and a boolean for whether we have visited or not.
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False) # assume the user is creating a input they havent been to yet

    def __str__(self):
        return f'{self.name} Visited? {self.visited}'
    

