import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Genre, Movie, UserProfile

@require_http_methods(["GET", "POST"])
@csrf_exempt
def api_movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()

        data = []
        for m in movies:
            data.append({
	      "id": m.id,
	      "title": m.title,
	      "year": m.year,
	      "genres": list(m.genres.values_list('name', flat=True))
	  })

        return JsonResponse({"count": len(data), "results": data}, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        movie = Movie.objects.create(
	  title=body.get("title"),
	  year=body.get("year"),
	  description=body.get("description", "")
        )
        return JsonResponse({"status": "created", "id": movie.id}, status=201)
    return None


@require_http_methods(["GET"])
def api_search(request):
    query = request.GET.get('q', '')

    if not query:
        return JsonResponse({"status": "error", "message": "Parameter 'q' is required"}, status=400)

    movies = Movie.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ).distinct()

    data = []
    for m in movies:
        data.append({
            "id": m.id,
            "title": m.title,
            "year": m.year,
            "description": m.description,
            "genres": list(m.genres.values_list('name', flat=True))
        })

    return JsonResponse({
        "status": "ok",
        "count": len(data),
        "query": query,
        "results": data
    }, safe=False)

@require_http_methods(["GET"])
def api_movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse({
        "id": movie.id,
        "title": movie.title,
        "year": movie.year,
        "description": movie.description
    })

@require_http_methods(["GET"])
def api_genres(request):
    genres = Genre.objects.all()
    data = [{"id": g.id, "name": g.name} for g in genres]
    return JsonResponse({"results": data}, safe=False)


