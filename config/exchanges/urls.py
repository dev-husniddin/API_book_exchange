from django.urls import path
from .views import ExchangeListCreateView, ExchangeDetailView

urlpatterns = [
    path('exchanges/', ExchangeListCreateView.as_view(), name='exchange-list-create'),
    path('exchanges/<int:pk>/', ExchangeDetailView.as_view(), name='exchange-detail'),
]
