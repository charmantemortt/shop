from rest_framework import serializers

from .models import Shop, Product, Stock


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'plu', 'name']

class StockSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='plu', queryset=Product.objects.all())
    shop = serializers.SlugRelatedField(slug_field='name', queryset=Shop.objects.all())

    class Meta:
        model = Stock
        fields = ['id', 'product', 'shop', 'quantity_on_shelf', 'quantity_in_order']