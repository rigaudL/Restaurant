from django.db import models
from django.contrib.auth.models import User
meal_type = (
    
    ("starters", "starters"),
    ("salads", "salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts","Desserts")
    
)

STATUS_CHOICES = (
    ("available", "Available"),
    ("not_available", "Not Available"),
)





class Item(models.Model):
    meal = models.CharField(max_length=1000, unique = True)
    descriPtiion = models.CharField(max_length = 2000)
    price = models.DecimalField(max_digits = 10 , decimal_places=2)
    meal_type = models.CharField(max_length = 200 ,choices = meal_type)
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meal