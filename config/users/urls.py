from django.urls import path
from .views import UserListCreateView
from .views import registration_view


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('register/', registration_view, name='registration_view'),
]
