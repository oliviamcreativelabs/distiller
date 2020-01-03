from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='cocktails'),
    path('<int:cocktail_id>', views.cocktail, name='cocktail'),
    path('search', views.search, name='search'),
]
