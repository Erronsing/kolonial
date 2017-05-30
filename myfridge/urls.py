from django.conf.urls import url
from . import views

app_name = 'myfridge'
urlpatterns = [
    url(r'^ingredients$', views.IngredientListView.as_view(), name='ingredient-list'),
    url(r'^ingredient/new/$', views.ingredient_new, name='ingredient-new'),
    url(r'^recipes$', views.RecipeListView.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)/$', views.RecipeDetailView.as_view(), name='recipe-detail'),
]