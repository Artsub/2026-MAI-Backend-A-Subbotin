from rest_framework import serializers
from .models import Genre, Movie, UserProfile
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = [
	  'id', 'title', 'description', 'year', 'duration',
	  'genres', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    favorites = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Movie.objects.all(),
        required=False
    )

    class Meta:
        model = UserProfile
        fields = [
	  'id', 'user', 'bio', 'avatar', 'location', 'birth_date',
	  'favorites', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
