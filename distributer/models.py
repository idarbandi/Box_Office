from django.db import models
from MovieCrawl.models import Movie


class Distributer(models.Model):
    name = models.CharField(null=True, max_length=32)
    web = models.CharField(null=True,max_length=35)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class MovieDistributer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='distributer')
    distributers = models.ForeignKey(Distributer, on_delete=models.CASCADE, related_name='movies')
    download_rate = models.BigIntegerField(null=True)

    def __str__(self):
        return f"{self.movie}\tHas\t{self.distributers}\tWith\t{self.download_rate} KB/S Download Rate"