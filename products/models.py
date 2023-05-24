from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    # image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=7, decimal_places=2)  # 99999.99
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    deposit = models.ForeignKey(
        "deposits.Deposit", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name
