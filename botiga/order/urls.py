from django.urls import path
from .views import get_all_orders, get_not_completed_orders, delete_not_completed_orders

urlpatterns = [
    path("", get_all_orders, name="get_all_orders"),
    path("not-completed/", get_not_completed_orders, name="get_not_completed_orders"),
    path("not-completed/", delete_not_completed_orders, name="delete_not_completed_orders")
]