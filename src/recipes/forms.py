from django import forms

## Search recipes ##

class RecipeSearchForm(forms.Form):
    search_name = forms.CharField(required=False, label="Search by name")
    search_ingredient = forms.CharField(required=False, label="Search by ingredient")

## User create a recipe form ##

class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=70, required=False)
    cooking_time = forms.IntegerField(help_text='in minutes', required=False)
    ingredients = forms.CharField(max_length=300, required=False)
    directions = forms.CharField(max_length=600, required=False)
    picture = forms.ImageField(required=False) 