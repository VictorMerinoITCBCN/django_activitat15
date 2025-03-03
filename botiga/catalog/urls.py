from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'catalog', ProductViewSet),
urlpatterns = [
    path("", include(router.urls))
]
