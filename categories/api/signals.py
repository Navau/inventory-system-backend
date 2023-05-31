from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
from categories.models import Category


# PONE EN NULL EL CAMPO CATEGORY DE PRODUCTOS, SI ES QUE LA CATEGORY SE DESACTIVA (ACTIVE = FALSE)
@receiver(post_save, sender=Category)
def update_relation_product_categories(sender, instance, **kwargs):
    if instance.active == False:
        Product.objects.filter(category=instance).update(category=None)


# post_save.connect(update_relation_product_categories, sender=Category)
