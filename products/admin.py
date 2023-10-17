from django.contrib import admin

from products.models import Basket, Product, ProductCategory

# Register your models here.

admin.site.register(ProductCategory)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category',]
    fields = ['name', 'price', 'quantity', 'category', 'image', 'description', 'stripe_product_price_id']
    search_fields = ('name', )
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp',]
    extra = 0
    readonly_fields = ('created_timestamp',)