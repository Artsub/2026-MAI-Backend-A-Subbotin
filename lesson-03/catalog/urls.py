# catalog/urls.py
from django.http import JsonResponse
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('api/profile/', views.api_profile, name='api_profile'),
    path('api/movies/', views.api_movies_list, name='api_movies_list'),
    path('api/movies/<int:movie_id>/', views.api_movie_detail, name='api_movie_detail'),
    path('api/genres/', views.api_genres, name='api_genres'),

]