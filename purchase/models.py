from django.contrib.auth.models import User
from django.db import transaction

from financial.models import Payment
from package.models import Package

from django.db import models


class Purchase(models.Model):
    PAID = 10
    NOT_PAID = -10

    PAID_STATUS = (
        (PAID, 'Paid'),
        (NOT_PAID, 'Not Paid')
    )

    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='purchase', on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    status = models.SmallIntegerField(choices=PAID_STATUS, default=NOT_PAID)
    payment = models.ForeignKey(Payment, related_name='purchase', on_delete=models.PROTECT)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.package} >> {self.user} >> {self.status}"

    @staticmethod
    def create_payment(package, user):
        return Payment.objects.create(amount=package.price, user=user)

    @classmethod
    def create(cls, package, user):
        if package.is_enable:
            with transaction.atomic():
                payment = cls.create_payment(package, user)
                purchase = cls.objects.create(
                    user=user, package=package,
                    price=package.price, payment=payment
                )
            return purchase
        return None
