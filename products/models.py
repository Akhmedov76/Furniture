from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextField
from django.utils.translation.trans_null import gettext_lazy as _

from common.models import BaseModel


class CategoryModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Category'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class TagModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Tag'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class BrandModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Brand'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class ColorModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Color name'))
    code = models.CharField(max_length=128, verbose_name=_('Color code'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')


class ProductModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Product name'))
    image1 = models.ImageField(upload_to='products/', verbose_name=_('Product image1'))
    image2 = models.ImageField(upload_to='products/', verbose_name=_('Product image2'))
    short_description = models.TextField()
    long_description = models.TextField()
    is_stock = models.BooleanField(default=True, verbose_name=_('Is stock'))
    sku = models.BooleanField(max_length=15, unique=True)
    quantity = models.PositiveIntegerField(default=1)
    discount_percentage = models.PositiveIntegerField(default=0,
                                                      validators=[MinValueValidator(0), MaxValueValidator(100)])

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    real_price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ManyToManyField(CategoryModel, related_name='category_products')
    tags = models.ManyToManyField(TagModel, related_name='tagged_products')
    colors = models.ManyToManyField(ColorModel, related_name='colored_products')

    brands = models.ForeignKey(BrandModel, related_name='products', on_delete=models.CASCADE)

    def is_discount(self):
        return True if self.discount_percentage != 0 else False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImageModel(BaseModel):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', verbose_name=_('Product image'))
