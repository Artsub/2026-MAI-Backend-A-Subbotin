from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def api_profile(request):
    return JsonResponse({
        "status": "ok",
        "data": {
	  "username": "demo_user",
	  "email": "demo@example.com",
	  "favorites_count": 0
        }
    }, status=200)


@require_http_methods(["GET", "POST"])
def api_movies_list(request):
    if request.method == "GET":
        return JsonResponse({
	  "status": "ok",
	  "data": [
	      {"id": 1, "title": "Inception", "genre": "Sci-Fi", "year": 2010},
	      {"id": 2, "title": "The Matrix", "genre": "Sci-Fi", "year": 1999},
	      {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014}
	  ],
	  "count": 3
        }, status=200)

    elif request.method == "POST":
        return JsonResponse({
	  "status": "ok",
	  "message": "Movie creation stub"
        }, status=201)
    return None


@require_http_methods(["GET"])
def api_movie_detail(request, movie_id):
    return JsonResponse({
        "status": "ok",
        "data": {
	  "id": movie_id,
	  "title": f"Movie #{movie_id}",
	  "description": "Stub description",
	  "genre": "Stub Genre",
	  "year": 2024,
	  "rating": 8.5
        }
    }, status=200)


@require_http_methods(["GET"])
def api_genres(request):
    return JsonResponse({
        "status": "ok",
        "data": [
	  {"id": 1, "name": "Action"},
	  {"id": 2, "name": "Comedy"},
	  {"id": 3, "name": "Drama"},
	  {"id": 4, "name": "Sci-Fi"}
        ]
    }, status=200)