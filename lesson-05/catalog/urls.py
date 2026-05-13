# catalog/urls.py
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('api/search/', views.MovieSearchView.as_view(), name='api_search'),
    path('api/movies/', views.MovieListCreateView.as_view(), name='api_movies_list'),
    path('api/movies/<int:movie_id>/', views.MovieDetailView.as_view(), name='api_movie_detail'),
    path('api/genres/', views.GenreListView.as_view(), name='api_genres'),
]
