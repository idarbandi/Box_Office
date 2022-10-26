import uuid

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from khayyam.jalali_datetime import JalaliDatetime

from django.db import models

from financial.utils.zarinpal import zarinpal_request_handler, zarinpal_payment_checker


class Gateway(models.Model):
    """ 💳 """
    FUNCTION_ZARINPAL = 'zarinpal'

    GATEWAY_FUNCTION = (
        (FUNCTION_ZARINPAL, 'Zarinpal'),
    )

    title = models.CharField(max_length=180, verbose_name=_('gateway title'))
    gateway_request_url = models.CharField(max_length=150, verbose_name=_('request url'), null=True, blank=True)
    gateway_verify_url = models.CharField(max_length=150, verbose_name=_('verify url'), null=True, blank=True)
    gateway_code = models.CharField(max_length=12, verbose_name=_('gateway code'), choices=GATEWAY_FUNCTION)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    auth_data = models.TextField(verbose_name=_('auth data'), null=True, blank=True)

    created_time = models.DateTimeField(default=JalaliDatetime.now)
    modified_time = models.DateTimeField(default=JalaliDatetime.now)

    class Meta:
        verbose_name = _('gateway')
        verbose_name_plural = _('gateways')

    def __str__(self):
        return self.title

    def get_request_handler(self):
        handlers = {
            self.FUNCTION_ZARINPAL: zarinpal_request_handler
        }
        return handlers[self.gateway_code]

    def get_verify_handler(self):
        handlers = {
            self.FUNCTION_ZARINPAL: zarinpal_payment_checker
        }
        return handlers[self.gateway_code]


class Payment(models.Model):
    """ 💸 """
    invoice_number = models.UUIDField(max_length=150, verbose_name=_('invoice number'),
                                      unique=True, default=uuid.uuid4())
    amount = models.IntegerField(verbose_name=_('amount'))
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, related_name='payments', verbose_name=_('gateways'),
                                null=True, blank=True)
    is_paid = models.BooleanField(verbose_name=_('is paid'), default=False)
    payment_log = models.TextField(verbose_name=_('log'), blank=True)
    user = models.ForeignKey(User, related_name='payments', verbose_name=_('user'), on_delete=models.SET_NULL,
                             null=True)
    authority = models.CharField(max_length=64, verbose_name=_('authority'), blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._b_is_paid = self.is_paid

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return self.invoice_number.hex

    def get_data(self):
        data = dict(merchant_id=self.gateway.auth_data,
                    amount=self.amount,
                    detail='خرید اشتراک',
                    user_email=self.user.email,
                    user_phone_number='0912256487',
                    callback='http://127.0.0.1:8000/MovieCrawl/movie/account/financial/verify/')
        return data

    def verify(self, data):
        handler = self.gateway.get_verify_handler()
        if not self.is_paid and handler is not None:
            handler(**data)
        return self.is_paid

    @property
    def bank_page(self):
        handler = self.gateway.get_request_handler()
        if handler is not None:
            data = self.get_data()
            link, authority = handler(**data)
            if authority:
                self.authority = authority
                self.save()
            return link
