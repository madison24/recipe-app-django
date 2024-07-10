from django.urls import path 
from .views import home
from .views import AllRecipeView, RecipeDetailView
from .views import create_view, about_view

app_name= "recipes"

urlpatterns = [
    path("", home),
    path('list/', AllRecipeView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('create/', create_view, name='create'),
    path('about/', about_view, name='about'),

]
