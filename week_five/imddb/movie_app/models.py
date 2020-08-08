from django.db import models

# create a director model
class Director(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# create a movie model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    director = models.ForeignKey(Director, related_name="movies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# create an actor table
# movies may have many actors
# actors may be in many movies
class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='actors')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)