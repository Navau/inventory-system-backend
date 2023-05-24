from django.db import models


class Deposit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    address = models.TextField(max_length=2000)
    capacity = models.PositiveIntegerField(
        default=0
    )  # Puede tambien ser por productos, pero hay que crear una nueva aplicacion llamada capacityDeposit
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
