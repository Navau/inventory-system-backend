from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from deposits.models import Deposit
from deposits.api.serializers import DepositSerializer


class DepositApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = DepositSerializer
    queryset = Deposit.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["active"]
    search_fields = ["name", "description", "update_at"]
