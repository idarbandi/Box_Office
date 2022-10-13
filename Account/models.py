from django.contrib.auth.models import User
from django.db import models
from khayyam.jalali_datetime import JalaliDatetime

from MovieCrawl.models import Movie


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='useraccount', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    def add(self, film, qty):
        if self.basket.filter(movie=film).exists():
            movie_basket = self.basket.filter(movie=film).first()
            movie_basket.quantity += qty
            movie_basket.save()
        else:
            movie_basket = self.basket.create(movie=film, quantity=qty)
        return movie_basket


class BasketLines(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='basket')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='purchase')
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.account}\t==>{self.quantity}\tDisks of {self.movie}"
