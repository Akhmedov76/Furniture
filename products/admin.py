from django.contrib import admin

from products.forms import ColorPickerForm
from products.models import CategoryModel, TagModel, BrandModel, ColorModel, ProductModel, ProductImageModel


@admin.register(CategoryModel)
class CategoryModel(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    search_fields = ('name', 'code',)
    list_filter = ('created_at',)
    form = ColorPickerForm


class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'real_price', 'discount_percentage']
    search_fields = ('name', 'short_description',)
    list_filter = ('created_at', 'updated_at', 'category',)
    inlines = [ProductImageModelAdmin]
    readonly_fields = ('real_price',)
