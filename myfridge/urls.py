from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ingredients$', views.ingredient_list, name='ingredient_list'),
    url(r'^ingredient/new/$', views.ingredient_new, name='ingredient_new'),
    url(r'^recipes$', views.RecipeListView.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)/$', views.RecipeDetailView.as_view(), name='recipe-detail'),
]