import math
from decimal import ROUND_HALF_UP, Decimal

from django.db import models


class Receipt(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    total_amount_payable = models.DecimalField(max_digits=19, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def formatted_amount(self):
        return self.total_amount_payable.quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
