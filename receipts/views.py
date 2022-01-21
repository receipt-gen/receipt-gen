from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import transaction
from django.template.loader import render_to_string

from rest_framework import mixins, serializers, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from receipts.models import Receipt
from receipts.serializers import ReceiptSerializer
from receipts.utils import convert_html_to_pdf


class ReceiptViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        receipt = serializer.save()

        html_string = render_to_string("receipts/receipt.html", {"receipt": receipt})
        pisa_status, io_bytes = convert_html_to_pdf(html_string)

        if pisa_status.err:  # pylint: disable=no-member
            raise serializers.ValidationError(
                "Sorry, we had some errors generating the PDF of your receipt."
            )

        default_storage.save(
            f"receipts/receipt_{receipt.pk}.pdf", ContentFile(io_bytes.getvalue())
        )

        msg = "Receipt PDF has been generated."
        return Response(data={"detail": msg}, status=status.HTTP_201_CREATED)
