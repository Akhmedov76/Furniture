from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def my_handler(sender, instance, **kwargs):
    if instance.is_discount():
        discount_decimal = Decimal(instance.discount_percentage) / Decimal(100)
        instance.real_price = instance.price - (instance.price * discount_decimal)
    else:
        instance.real_price = instance.price
