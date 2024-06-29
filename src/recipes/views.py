from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .utils import get_popular_ingredients_chart

import pandas as pd 


# Create your views here.
def home(request):
    return render(request, "recipes/recipes_home.html")

class AllRecipeView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/all_recipes.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        search_name = self.request.GET.get("search_name")
        search_ingredient = self.request.GET.get("search_ingredient")

        if search_name:
            queryset = queryset.filter(name__icontains=search_name)
        if search_ingredient:
            queryset = queryset.filter(ingredients__icontains=search_ingredient)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        df = pd.DataFrame(list(queryset.values('id', 'name', 'cooking_time', 'pic')))
        recipes = df.to_dict("records") if not df.empty else []

        for recipe in recipes:
            recipe_instance = Recipe.objects.get(pk=recipe["id"])
            recipe["get_absolute_url"] = recipe_instance.get_absolute_url()
            recipe["pic_url"] = recipe_instance.pic.url if recipe_instance.pic else None

        context["object_list"] = recipes

        num_results = len(context["object_list"])
        title_parts = []

        search_name = self.request.GET.get("search_name")
        search_ingredient = self.request.GET.get("search_ingredient")

        if search_name:
            title_parts.append(f"'{search_name}' in the name")
        if search_ingredient:
            title_parts.append(f"'{search_ingredient}' in the ingredients")

        if title_parts:
            context['main_title'] = "Search results:"
            recipe_word = "Recipe" if num_results == 1 else "Recipes"
            details_intro = f"{recipe_word} with "
            context['search_details'] = details_intro + ", ".join(title_parts)
        else:
            context['main_title'] = "All recipes"
            context['search_results'] = "Search results"
        
        recipes_list = list(queryset.values('id', 'name','cooking_time', 'ingredients', 'directions', 'pic'))

        context["search_form"] = RecipeSearchForm(self.request.GET)
        context["show_all_recipes_button"] = bool(self.request.GET)
        context["popular_ingredients_chart"] = get_popular_ingredients_chart(recipes_list)

        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'search_params': self.request.GET.urlencode()
        })
        return context
