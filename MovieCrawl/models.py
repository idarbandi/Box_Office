from django.db import models
from khayyam.jalali_datetime import JalaliDatetime


class Director(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    # INT = 1
    # STRING = 2
    # FLOAT = 3
    #
    # initial_choices = (
    #     (INT, 'Integer'),
    #     (STRING, 'String'),
    #     (FLOAT, 'Float'),
    #
    # )

    name = models.CharField(max_length=32)
    director_id = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies')
    actor_id = models.ForeignKey(Actor, on_delete=models.PROTECT, related_name='actrs_movies')
    year = models.IntegerField(blank=True)
    rate = models.FloatField(blank=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    age_res = models.CharField(max_length=10)
    summary = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    awards = models.CharField(max_length=32)
    register_date = models.DateTimeField(default=JalaliDatetime.now)
    modify_date = models.DateTimeField(default=JalaliDatetime.now)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DirMovie(models.Model):
    dir_id = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='directors')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='directorsmovies')

    def __str__(self):
        return f"{self.movie_id} , {self.dir_id}"


class ActorMovie(models.Model):
    actor_id = models.ForeignKey(Actor, on_delete=models.PROTECT, related_name='moviesactors')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='atorsmovies')

    def __str__(self):
        return f"{self.actor_id} , {self.movie_id}"


class GenreMovie(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='moviegenres')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='genresmovies')

    def __str__(self):
        return f"{self.genre_id} , {self.movie_id}"
