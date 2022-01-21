from rest_framework.routers import DefaultRouter

from receipts.views import ReceiptViewSet

router = DefaultRouter()
router.register("receipts", ReceiptViewSet, basename="receipts")
