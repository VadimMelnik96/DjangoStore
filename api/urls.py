from django.urls import path, include

from api.views import ProductModelViewSet
from rest_framework import routers

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

    ]