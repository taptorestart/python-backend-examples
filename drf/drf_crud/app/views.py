from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer, CategorySerializer, BeverageSerializer
from app.models import Category, Beverage


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head']
    permission_classes = [permissions.IsAuthenticated]


class BeverageViewSet(viewsets.ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head']
    permission_classes = [permissions.IsAuthenticated]
