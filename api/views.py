from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductModelViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]