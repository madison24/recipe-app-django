from django.urls import path 
from .views import home
from .views import AllRecipeView
from .views import RecipeDetailView

app_name= "recipes"

urlpatterns = [
    path("", home),
    path('list/', AllRecipeView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]
