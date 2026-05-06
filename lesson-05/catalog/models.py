from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text='Продолжительность в минутах', blank=True, null=True)
    genres = models.ManyToManyField(
        Genre,
        related_name='movies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True, max_length=500)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        help_text='Пользователь, добавивший в избранное'
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='favorited_by',
        help_text='Фильм в избранном'
    )
    note = models.CharField(max_length=200, blank=True, help_text='Личная заметка к фильму')
    added_at = models.DateTimeField(auto_now_add=True)
