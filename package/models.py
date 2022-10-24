from django.db import models
from khayyam.jalali_date import JalaliDate


class Package(models.Model):
    title = models.CharField(max_length=48)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    days = models.PositiveSmallIntegerField()
    is_enable = models.BooleanField(default=True)

    created_day = models.DateField(default=JalaliDate.today)
    created_time = models.TimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Benefits(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='benefits')
    description = models.CharField(max_length=25)
