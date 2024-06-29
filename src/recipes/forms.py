from django import forms

class RecipeSearchForm(forms.Form):
    search_name = forms.CharField(required=False, label="Search by name")
    search_ingredient = forms.CharField(required=False, label="Search by ingredient")
