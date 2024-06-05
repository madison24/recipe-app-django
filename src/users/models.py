from django.db import models
from recipes.models import Recipe

# Create your models here.
class User(models.Model):
    name = models.CharField(help_text = 'Enter your name', max_length=120)
    stored_recipes = models.ForeignKey(Recipe, on_delete = models.CASCADE)

    def __str__(self):
        return f" {self.name}, stored recipes: {self.stored_recipes.name}"