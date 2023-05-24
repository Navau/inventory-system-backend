from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from deposits.models import Deposit
from deposits.api.serializers import DepositSerializer


class DepositApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = DepositSerializer
    queryset = Deposit.objects.all().order_by("id")
