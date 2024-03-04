from django.shortcuts import render
from .serializers import CategorySerializers, BrandSerializers, ProductSerializers
from .models import Category, Brand, Product
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self,request):
        serializers = CategorySerializers(self.queryset, many=True)
        return Response(serializers.data)
    


class BrandView(viewsets.ViewSet):
    queryset = Brand.objects.all()
    # print(queryset)

    def list(self,request):
        serializers = BrandSerializers(self.queryset, many=True)
        return Response(serializers.data)
    


class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    print(queryset)

    def list(self,request):
        serializers = ProductSerializers(self.queryset, many=True)
        return Response(serializers.data)
    
    def create(self, request):
        serializers  = ProductSerializers(request.data)
        return Response(serializers.data)

