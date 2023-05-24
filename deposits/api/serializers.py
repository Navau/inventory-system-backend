from rest_framework.serializers import ModelSerializer
from deposits.models import Deposit


class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            "id",
            "name",
            "description",
            "address",
            "capacity",
            "active",
            "created_at",
            "update_at",
        ]
