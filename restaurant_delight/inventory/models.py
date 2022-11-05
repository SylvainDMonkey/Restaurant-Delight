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
    ingredient_name = models.CharField(max_length=50)
    type_of_ingredients = models.CharField(max_length=2, choices=TYPE_OF_INGREDIENTS, default='OT')
    available_quantity = models.IntegerField(default=0)
    unitary_price = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.ingredient_name} bought {self.unitary_price}$ has currently {self.available_quantity} in stock"

class MenuItem(models.Model):
    menu_title = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.menu_title}"

class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu.menu_title} include {self.ingredient.ingredient_name}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(RecipeRequirement, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item}"
