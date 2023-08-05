from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
from deposits.models import Deposit


@receiver(post_save, sender=Deposit)
def update_relation_product_deposits(sender, instance, **kwargs):
    if instance.active == False:
        Product.objects.filter(deposit=instance).update(deposit=None)