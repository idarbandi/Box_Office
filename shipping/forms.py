from django import forms
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
    def __init__(self, user):
        self.user = user
        self.address_list = forms.ModelChoiceField(queryset=user.address.all())