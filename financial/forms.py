from django import forms
from khayyam.jalali_date import JalaliDate


class PayForm(forms.Form):
    price = forms.FloatField(widget=forms.NumberInput)
    expiration_date = forms.DateField(initial=JalaliDate.today)
