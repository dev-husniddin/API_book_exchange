from rest_framework import generics
from .models import Exchange
from .serializers import ExchangeSerializer

class ExchangeListCreateView(generics.ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class ExchangeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
