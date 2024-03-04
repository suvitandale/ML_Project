from rest_framework import serializers
from .models import Category, Brand, Product

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    Category = CategorySerializers()

    class Meta:
        model = Product
        fields = "__all__"

    def create_object(self, val_data):
        product = Product(
            name=val_data['name'],
            description=val_data['description'],
            is_digital=val_data['is_digital'],
            brand=val_data['brand'],
            Category=val_data['category']        )
        product.save()
        return product