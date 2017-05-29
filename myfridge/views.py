from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient

def ingredient_list(request):
	ingredients = Ingredient.objects.order_by('name')
	template = loader.get_template('myfridge/ingredient_list.html')
	context = {'ingredients': ingredients}
	return render(request, 'myfridge/ingredient_list.html', context)
