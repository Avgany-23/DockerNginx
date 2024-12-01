from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    positions = ProductPositionSerializer(many=True)

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        stock_products = [StockProduct(stock=stock,
                                       product=pos['product'],
                                       quantity=pos['quantity'],
                                       price=pos['price'])
                          for pos in positions]
        StockProduct.objects.bulk_create(stock_products)
        return stock

    def update(self, instance, validated_data):
        position = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for pos in position:
            product = pos.pop('product')
            StockProduct.objects.update_or_create(
                stock=stock,
                product=product,
                defaults=pos
            )
        return stock
