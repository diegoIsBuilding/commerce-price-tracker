# Create your models here.
# backend/tracker/models.py

from django.db import models

class Product(models.Model):
    #Create a Product model that contains the fields 
    #name, url, current_price
    #This model will map to a single database table
    name = models.CharField(max_length=255)
    url = models.URLField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as necessary

    def __str__(self):
        return self.name

# You can add more models for Price History, Users, etc.
