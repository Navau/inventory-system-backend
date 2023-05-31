from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from categories.models import Category
from categories.api.serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["active"]
    search_fields = ["name", "description", "update_at"]
