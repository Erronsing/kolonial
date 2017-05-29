from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ingredients$', views.ingredient_list, name='ingredient_list'),
    url(r'^ingredient/new/$', views.ingredient_new, name='ingredient_new')
]