from rest_framework.serializers import ModelSerializer
from products.models import Product

from categories.api.serializers import CategorySerializer
from deposits.api.serializers import DepositSerializer


class ProductSerializer(ModelSerializer):
    category_data = CategorySerializer(source="category", read_only=True)
    deposit_data = DepositSerializer(source="deposit", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "active",
            "created_at",
            "update_at",
            "category",
            "category_data",
            "deposit",
            "deposit_data",
        ]
