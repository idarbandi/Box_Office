from django import forms

from shipping.models import shipping


class shippingForm(forms.ModelForm):
    class Meta:
        model = shipping
        exclude = ('user',)

