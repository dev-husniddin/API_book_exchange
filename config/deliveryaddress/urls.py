from django.urls import path
from .views import ShippingAddressListCreateView, ShippingAddressDetailView

urlpatterns = [
    path('addresses/', ShippingAddressListCreateView.as_view(), name='shippingaddress-list-create'),
    path('addresses/<int:pk>/', ShippingAddressDetailView.as_view(), name='shippingaddress-detail'),
]
