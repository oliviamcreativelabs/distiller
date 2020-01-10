from django.urls import path

from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('reviews/<review_id>', views.review_detail, name='review_detail'),
    path('whiskey', views.whiskey_list, name='whiskey_list'),
    path('whiskey/', views.whiskey_detail, name='whiskey_detail'),
    path('whiskey/<whiskey_id>/add_review', views.add_review, name='add_review'),
]

