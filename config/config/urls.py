from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('config.users.urls')),  # Подключение URL маршрутов пользователей
    path('api/', include('books.urls')),  # Подключение URL-маршрутов приложения "books"
    path('api/', include('authors.urls')),  # Подключение URL-маршрутов приложения "authors"
    path('api/', include('categories.urls')),  # Подключение URL-маршрутов приложения "categories"
    path('api/', include('deliveryaddress.urls')),  # Подключение URL-маршрутов приложения "deliveryaddress"
    path('api/', include('exchanges.urls')),  # Подключение URL-маршрутов приложения "exchanges"
    path('api/', include('orders.urls')),  # Подключение URL-маршрутов приложения "orders"


]
