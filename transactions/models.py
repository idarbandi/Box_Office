from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from khayyam.jalali_datetime import JalaliDatetime
from django.db.models import Sum, Count, Q


class transaction(models.Model):
    CHARGE = 1
    CREDIT = 2
    TRANSFER_RECEIVE = 3
    TRANSFER_SENT = 4

    trans_types = [
        (CHARGE, "charge"),
        (TRANSFER_SENT, "variz"),
        (TRANSFER_RECEIVE, "daryaft"),
        (CREDIT, "cash")
    ]
    user = models.ForeignKey(User, related_name='user_trans', on_delete=models.RESTRICT)
    type = models.PositiveIntegerField(choices=trans_types, default=CREDIT)
    amount = models.BigIntegerField()
    updateDate = models.DateTimeField(default=JalaliDatetime.today)

    def __str__(self):
        return f"\t{self.user},\t{self.get_type_display()}\t{self.amount}"

    @classmethod
    def calculate_all_users_balance(cls):
        pos = Sum('user_trans__amount', filter=Q(user_trans__type=1))
        neg = Sum('user_trans__amount', filter=Q(user_trans__type__in=[2, 3]))
        users = User.objects.all().annotate(total=Count('user_trans'), balance=Coalesce(pos, 0) - Coalesce(neg, 0))
        for usr in users:
            final_balance = f"{usr.total}, {usr.balance}"
        return final_balance

    @classmethod
    def calculate_user_balance(cls, user):
        pos = Sum('amount', filter=Q(type__in=[1, 3]))
        neg = Sum('amount', filter=Q(type__in=[2, 4]))
        users = user.user_trans.all().aggregate(balance=Coalesce(pos, 0) - Coalesce(neg, 0))
        return users.get('balance', 0)


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_balance')
    balance = models.FloatField(null=True)
    moment = models.DateTimeField(auto_now_add=JalaliDatetime.now)


    @classmethod
    def record_balance(cls):
        bal = transaction.calculate()
