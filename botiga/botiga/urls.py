from django.urls import path, include

urlpatterns = [
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
    path("catalog/v1/", include("catalog.urls")),
    path("payment/", include("payment.urls"))
]
