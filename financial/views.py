from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from financial.forms import PayForm
from financial.models import Payment, Gateway
from financial.utils.zarinpal import zarinpal_payment_checker, zarinpal_request_handler


class Pay(View):
    template_name = 'pay.html'

    def get(self, request, invoice_number, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404
        gateway = Gateway.objects.get(is_enable=True)

        return render(request, self.template_name, {"payment": payment, "gateway": gateway})


class PostGateway(View):
    def get(self, request, invoice_number, gateway_code, *args, **kwargs):
        try:
            gateway = Gateway.objects.get(gateway_code=gateway_code)
        except Gateway.DoesNotExist:
            raise Http404

        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404

        payment.gateway = gateway
        payment.save()
        payment_link = payment.bank_page
        if payment_link:
            return redirect(payment_link)
        gateways = Gateway.objects.filter(is_enable=True)

        return render(request, 'pay.html', {"payment": payment, "gateways": gateways})
