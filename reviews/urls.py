from django.urls import path

from . import views

app_name = 'reviews' 

urlpatterns = [
    path('', views.review, name='review'),
    path('reviews/<int:review_id>', views.review_detail, name='review_detail'),
    path('whiskey', views.whiskey_list, name='whiskey_list'),
    path('whiskey/', views.whiskey_detail, name='whiskey_detail'),
    path('whiskey/<int:whiskey_id>/add_review', views.add_review, name='add_review'),
]
