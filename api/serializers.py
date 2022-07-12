from rest_framework import serializers
from shop.models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'slug', 'image', 'description','category', 'price','available','created','updated')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        