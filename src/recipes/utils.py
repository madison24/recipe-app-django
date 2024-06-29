from .models import Recipe
from collections import Counter
from io import BytesIO
import base64
import matplotlib.pyplot as plt 

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_popular_ingredients_chart(recipes):
    all_ingredients = []
    for recipe in recipes:
        ingredients_list = recipe['ingredients'].split(',')
        normalized = [ingredient.strip().lower() for ingredient in ingredients_list]
        all_ingredients.extend(normalized)

    ingredient_counts = Counter(all_ingredients)
    ingredients, counts = zip(*ingredient_counts.most_common(10)) if all_ingredients else ([], [])

    plt.switch_backend('AGG')
    plt.figure(figsize=(6,4))

    if ingredients and counts:
        plt.bar(ingredients, counts, color='#d44d28')
        plt.xlabel('Ingredient')
        plt.ylabel('# of Recipes')
        plt.title('Ingredients by Popularity')
        plt.xticks(rotation=45)
    else:
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center')
    plt.tight_layout()

    chart = get_graph()
    plt.close()
    return chart