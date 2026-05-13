from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all().prefetch_related('genres')
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
	  "status": "created",
	  "id": serializer.instance.id
        }, status=status.HTTP_201_CREATED)


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.prefetch_related('genres')
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'


class MovieSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '').strip()

        if not query:
            return Response(
	      {"status": "error", "message": "Parameter 'q' is required"},
	      status=status.HTTP_400_BAD_REQUEST
	  )

        movies = Movie.objects.filter(
	  Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct().prefetch_related('genres')

        serializer = MovieSerializer(movies, many=True)
        return Response({
	  "status": "ok",
	  "count": movies.count(),
	  "query": query,
	  "results": serializer.data
        })


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer