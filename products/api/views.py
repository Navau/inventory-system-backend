from rest_framework.viewsets import ModelViewSet

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from products.models import Product
from products.api.serializers import ProductSerializer


class ProductApiViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category", "deposit", "active"]
    search_fields = [
        "name",
        "description",
        "price",
        "stock",
        "update_at",
        "category__name",
        "deposit__name",
        "active",
    ]

    def create(self, request, *args, **kwargs):
        print("REQUEST_DATA", request.data)
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print("REQUEST_DATA", request.data)
        return super().partial_update(request, *args, **kwargs)

    # def pre_save(self, obj):
    #     obj.update_at = timezone.now()
