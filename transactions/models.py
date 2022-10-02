from django.db import models
from django.contrib.auth.models import User
from khayyam.jalali_datetime import JalaliDatetime


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
        return ','.join(f"\t{self.user},\t{self.type}\t{self.amount}")


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_balance')
    balance = models.FloatField(null=True)
    moment = models.DateTimeField(auto_now_add=JalaliDatetime.now)




