from django.contrib.auth.models import User
from django.db import models
from khayyam.jalali_datetime import JalaliDatetime

from MovieCrawl.models import Movie


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='useraccount', null=True, blank=True)
    created_time = models.DateTimeField(default=JalaliDatetime.now)

    def __str__(self):
        return f"{self.user}\t{self.created_time}"


class BasketLines(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='basket')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='purchase')
    quantity = models.PositiveIntegerField(default=1)
