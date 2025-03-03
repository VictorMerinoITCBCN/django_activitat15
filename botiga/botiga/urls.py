from django.urls import path, include

urlpatterns = [
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls"))
]
