from django.db import models

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	ingredients = models.ManyToManyField(Ingredient, 
		through='RecipeIngredient')

	def __str__(self):
		return self.title

class RecipeIngredient(models.Model):
	ingredient = models.ForeignKey(Ingredient,
		on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe,
		on_delete=models.CASCADE)
	quantity = models.IntegerField()

class Fridge(models.Model):
	ingredients = models.ManyToManyField(Ingredient,
		through='FridgeContents')
	
class FridgeContents(models.Model):
	ingredient = models.ForeignKey(Ingredient,
		on_delete=models.CASCADE)
	fridge = models.ForeignKey(Fridge,
		on_delete=models.CASCADE)
	quantity = models.IntegerField()

