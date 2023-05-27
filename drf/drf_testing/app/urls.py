from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.views import CategoryViewSet, BeverageViewSet

router = SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'beverages', BeverageViewSet, basename='beverage')

urlpatterns = [
    path('', include(router.urls)),
]
