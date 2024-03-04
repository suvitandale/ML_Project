from django.shortcuts import render
from .serializers import CategorySerializers
from .models import Category, Brand, Product
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self,request):
        serializers = CategorySerializers(self.queryset, many=True)
        return Response(serializers.data)