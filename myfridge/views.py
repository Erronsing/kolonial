from django.shortcuts import render, redirect
from django.views import generic
from django.template import loader
from django.urls import reverse
from .models import Ingredient, Recipe, Fridge 
from .forms import IngredientForm

def index(request):
	return render(request, 'myfridge/index.html', {})

class RecipeListView(generic.ListView):
	template_name = 'myfridge/recipe_list.html'
	context_object_name = 'recipe_list'

	def get_queryset(self):
		return Recipe.objects.order_by('title')

class RecipeDetailView(generic.DetailView):
	model = Recipe
	template_name = 'myfridge/recipe_detail.html'

	def get_context_data(self, **kwargs):
		context = super(RecipeDetailView, self).get_context_data(**kwargs)
		return context

class IngredientListView(generic.ListView):
	template_name = 'myfridge/ingredient_list.html'
	context_object_name = 'ingredients'

	def get_queryset(self):
		return Ingredient.objects.order_by('name')

def ingredient_new(request):
	if request.method == "POST":
		form = IngredientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myfridge:ingredient-list')
	else:
		form = IngredientForm
	return render(request, 'myfridge/ingredient_edit.html', {'form': form})

class FridgeListView(generic.ListView):
	template_name = 'myfridge/fridge_list.html'
	context_object_name = 'fridge_list'

	def get_queryset(self):
		return Fridge.objects

class FridgeDetailView(generic.DetailView):
	model = Fridge
	template_name = 'myfridge/fridge_detail.html'

	def get_context_data(self, **kwargs):
		context = super(FridgeDetailView, self).get_context_data(**kwargs)
		return context

class FridgeMatchView(generic.DetailView):
	model = Fridge
	template_name = 'myfridge/fridge_match.html'