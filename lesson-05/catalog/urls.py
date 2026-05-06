# catalog/urls.py
from django.http import JsonResponse
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('api/search/', views.api_search, name='api_search'),
    path('api/movies/', views.api_movies_list, name='api_movies_list'),
    path('api/movies/<int:movie_id>/', views.api_movie_detail, name='api_movie_detail'),
    path('api/genres/', views.api_genres, name='api_genres'),

]