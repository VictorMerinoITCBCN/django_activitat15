from django.urls import path
from .views.cart_item import get_all_cart_items, get_cart_item, create_cart_item, delete_cart_item, patch_cart_item
from .views.cart import get_all_carts, get_cart, create_cart, delete_cart, create_order_from_cart

urlpatterns = [
    path("", get_all_carts, name="get_all_carts"),
    path("<int:id>/", get_cart, name="get_cart"),
    path("", create_cart, name="create_cart"),
    path("<int:id>/", delete_cart, name="delete_cart"),

    path("item/", get_all_cart_items, name="get_all_cart_items"),
    path("item/<int:id>/", get_cart_item, name="get_cart_item"),
    path("item/", create_cart_item, name="create_cart_item"),
    path("item/<int:id>/", delete_cart_item, name="delete_cart_item"),
    path("item/<int:id>/", patch_cart_item, name="patch_cart_item"),

    path("buy/<int:id>/", create_order_from_cart, name="create_order_from_cart")
]