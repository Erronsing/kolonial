from django.shortcuts import render, redirect
from django.views import generic
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient
from .forms import IngredientForm


def ingredient_list(request):
	ingredients = Ingredient.objects.order_by('name')
	template = loader.get_template('myfridge/ingredient_list.html')
	context = {'ingredients': ingredients}
	return render(request, 'myfridge/ingredient_list.html', context)

def ingredient_new(request):
	if request.method == "POST":
		form = IngredientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('ingredient_list')
	else:
		form = IngredientForm
	return render(request, 'myfridge/ingredient_edit.html', {'form': form})
