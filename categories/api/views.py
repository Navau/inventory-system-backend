from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")
