from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    city = models.CharField(max_length=32, blank=True)
    zipcode = models.TextField(max_length=16)
    address = models.TextField(max_length=100)
    number = PhoneNumberField(blank=True, null=True, region='IR', max_length=14)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} at {self.city}"

