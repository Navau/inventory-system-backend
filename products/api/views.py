from rest_framework.viewsets import ModelViewSet

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product
from products.api.serializers import ProductSerializer


class ProductApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "deposit"]

    def create(self, request, *args, **kwargs):
        print("REQUEST_DATA", request.data)
        return super().create(request, *args, **kwargs)
