from django.shortcuts import render
from .serializers import ProductSerializer,UserSerializer
from shop.models import Product
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets,mixins
from django.contrib.auth.models import User

class ProductViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserViewSet(mixins.RetrieveModelMixin,  
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)





# class ProductList(ListAPIView):
#     queryset =  Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset =  Product.objects.filter(available=True)
#     serializer_class = ProductSerializer

# class ProductAdd(CreateAPIView):
#     queryset =  Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
