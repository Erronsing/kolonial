from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	published_date = models.DateTimeField(null=True)
	ingredients = models.ManyToManyField(Ingredient, 
		through='RecipeIngredient')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class RecipeIngredient(models.Model):
	ingredient = models.ForeignKey(Ingredient,
		on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe,
		on_delete=models.CASCADE)
	quantity = models.IntegerField()

class Fridge(models.Model):
	owner = models.CharField(max_length=100, default='')
	ingredients = models.ManyToManyField(Ingredient,
		through='FridgeContents')

	def __str__(self):
		if self.owner:
			return "%s's fridge" % (self.owner)
		else:
			return "lost fridge"

	def matching_recipes(self):
		recipes = Recipe.objects.filter(
			ingredients__in=self.ingredients.all())
		matches = {}
		for recipe in recipes:
			matches[recipe] = matches.get(recipe, 0) + 1
		return matches


	
class FridgeContents(models.Model):
	ingredient = models.ForeignKey(Ingredient,
		on_delete=models.CASCADE)
	fridge = models.ForeignKey(Fridge,
		on_delete=models.CASCADE)
	quantity = models.IntegerField()

