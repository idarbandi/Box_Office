from django import forms
from django.contrib.auth.models import User

from shipping.models import shipping


class shippingForm(forms.ModelForm):
    class Meta:
        model = shipping
        exclude = ('user',)

    def clean_number(self):
        number = self.cleaned_data['number']
        if len(number) > 12:
            raise f"تعداد شماره ها از حد مجاز بیشتر است"
        return int(number)


class listForm(forms.Form):
    user = None
    address = forms.ChoiceField()

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(listForm, self).__init__(*args, **kwargs)

