from django.db import models

# Create your models here.
class Ingredients(models.Model):
    TYPE_OF_INGREDIENTS = [
        ('ME', 'Meat'),
        ('VE', 'Vegetable'),
        ('FI', 'Fish'),
        ('SP', 'Spice'),
        ('FR', 'Fruit'),
        ('OT', 'Other'),
    ]
    ingredient = models.CharField(max_length=50)
    type_of_ingredients = models.CharField(max_length=2, choices=TYPE_OF_INGREDIENTS, default='OT')
    available_quantity = models.IntegerField(default=0)
    unitary_price = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.ingredient} bought {self.unitary_price} has currently {self.available_quantity} in stock"

class MenuItem(models.Model):
    menu = models.CharField(max_length=100)

