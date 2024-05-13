from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text='in minutes')
    ingredients = models.CharField(max_length=300)
    directions = models.TextField(max_length=500)

    def calculate_difficulty(self):
        difficulty = 'Undefined'
        ingredients = self.ingredients.split(', ')
        num_ingredients = len(ingredients)

        if self.cooking_time < 10: 
            if num_ingredients < 4:
                difficulty = 'Easy'
            else:
                difficulty = 'Medium'
        else: 
            if num_ingredients < 4:
                difficulty = 'Intermediate'
            else:
                difficulty = 'Hard'

        return difficulty
    
    def __str__(self):
        return str(self.name) 