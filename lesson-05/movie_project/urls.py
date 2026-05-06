# movie_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def web_home(request):
    return JsonResponse({"page": "home", "message": "Welcome to Movie Catalog"}, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('web/', web_home, name='web_home'),

    path('', include('catalog.urls')),
]