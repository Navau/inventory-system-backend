from rest_framework.routers import DefaultRouter
from deposits.api.views import DepositApiViewSet

router_deposit = DefaultRouter()

router_deposit.register(
    prefix="deposits", basename="deposits", viewset=DepositApiViewSet
)
