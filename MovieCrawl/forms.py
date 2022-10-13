from django import forms

from Account.models import Account
from MovieCrawl.models import Movie


class AddToBasketForm(forms.Form):
    movie = forms.ModelChoiceField(queryset=Movie.objects.all(), widget=forms.HiddenInput)
    quantity = forms.IntegerField()

    def save(self, account):
        basket = account.add(
            film=self.cleaned_data.get('movie'),
            qty=self.cleaned_data.get('quantity')
        )

        return basket
