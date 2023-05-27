from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Category, Beverage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = '__all__'
