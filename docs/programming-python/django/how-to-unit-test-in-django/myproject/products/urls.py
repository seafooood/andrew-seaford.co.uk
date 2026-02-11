from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from .views import home

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]
