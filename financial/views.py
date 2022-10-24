from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from financial.forms import PayForm
from financial.utils.zarinpal import zarinpal_payment_checker, zarinpal_request_handler


# Create your views here.

class PayRequest(View):
    template_name = 'pay.html'
    form = PayForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form})

    def post(self, request, *args, **kwargs):
        form = PayForm(request.POST)

        if form.is_valid():
            payment_link, authority = zarinpal_request_handler(
                settings.ZARINPAL['merchant_id'], form.cleaned_data['price'], 'خرید اشتراک',
                'darbandidr99@gmail.com', '09195554213', settings.ZARINPAL['callback_request_url'],

            )
            if payment_link:
                return redirect(payment_link)
            return render(request, self.template_name, {"form": form})


class PayConfirm(View):
    template_name = 'callback.html'

    def get(self, request, *args, **kwargs):
        authority = request.GET.get('Authority')
        is_paid, ref_id = zarinpal_payment_checker(
            settings.ZARINPAL['merchant_id'],
            1000, authority
        )

        return render(request, self.template_name, {"is_paid": is_paid, "ref_id": ref_id})
