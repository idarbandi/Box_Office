from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from shipping.models import shipping


class shippingForm(forms.ModelForm):
    class Meta:
        model = shipping
        exclude = ('user',)
        labels = {'address': 'آدرس', 'number': 'شماره تلفن', 'city': 'شهر', 'zipcode': 'کدپستی'}

    def clean_number(self):
        number = self.cleaned_data['number']
        if len(number) > 14:
            raise ValidationError("تعداد شماره ها از حد مجاز بیشتر است")
        return number


