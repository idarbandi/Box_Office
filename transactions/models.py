from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from khayyam.jalali_datetime import JalaliDatetime
from django.db.models import Sum, Count, Q


class transaction(models.Model):
    CHARGE = 1
    TRANSFER = 2
    CREDIT = 3

    trans_types = [
        (CHARGE, "charge"),
        (TRANSFER, "transfer"),
        (CREDIT, "Credit")
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_trans')
    type = models.PositiveIntegerField(choices=trans_types, default=CREDIT)
    amount = models.IntegerField(null=True)
    updateDate = models.DateTimeField(default=JalaliDatetime.today)

    def __str__(self):
        return f"\t{self.user},\t{self.get_type_display()}\t{self.amount}"

    @classmethod
    def calculate(cls):
        pos_transaction = Sum('user_trans').filter(Q(transaction__type=1))
        neg_transaction = Sum('user_trans').filter(Q(transaction__type__in=[2, 3]))
        user = User.objects.all().aggregate(all_transactions=Count('user_trans'),
                                            balance=Coalesce(pos_transaction) - Coalesce(neg_transaction))
        return user


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_balance')
    balance = models.FloatField(null=True)
    moment = models.DateTimeField(auto_now_add=JalaliDatetime.now)
