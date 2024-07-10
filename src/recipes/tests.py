from django.test import TestCase
from .forms import RecipeSearchForm
from .models import Recipe
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CreateRecipeForm

## Recipe test ##

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create( 
            name='Tea',
            cooking_time=5,
            ingredients='Tea Leaves, Sugar, Water',
            directions='1- Boil water. 2- Add tea leaves. 3- Add sugar to taste.')
          
        
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_field = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_field, 'name')

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cooking_time, 'in minutes')

    def test_ingredients_length(self):
        recipe = Recipe.objects.get(id=1)
        ing_max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(ing_max_length, 300)
    
    def test_directions(self):
        recipe = Recipe.objects.get(id=1)
        dir_max_length = recipe._meta.get_field('directions').max_length
        self.assertEqual(dir_max_length, 500)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_difficulty_calc(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Easy')

## Recipe search test ##
        
class RecipeFormTest(TestCase):
    def test_form_validity(self):
        form_data = {
            'search_name': 'Grilled Cheese',
            'search_ingredient': 'Cheese'
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


## User create a recipe test ##

class RecipeAuthTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            cooking_time='5',
            ingredients='Test Ingredients',
            directions='Test directions'
        )
        self.login_url = reverse('login')
    
    def test_create_recipe(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('recipes:create'), {
            'name': 'New Recipe',
            'cooking_time': 20,
            'ingredients': 'Test Ingredients',
            'directions': 'Test directions'
        })
        self.assertIn(response.status_code, [200, 302])
