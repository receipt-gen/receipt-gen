from rest_framework import serializers

from receipts.models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = [
            "name",
            "address",
            "phone_number",
            "total_amount_payable",
        ]
