"""
URL configuration for my_project_API_book_exchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from my_app.views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    BookView,
    CategoryView,
    AuthorView,
    OrderView,
    ExchangeView,
    FavoritesView,
    UserReviewView,
    ShippingAddressView,
    # Добавьте импорты для остальных вьюшек
)

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/books/<int:book_id>/', BookView.as_view(), name='book-detail'),
    path('api/categories/<int:category_id>/', CategoryView.as_view(), name='category-detail'),
    path('api/authors/<int:author_id>/', AuthorView.as_view(), name='author-detail'),
    path('api/orders/<int:order_id>/', OrderView.as_view(), name='order-detail'),
    path('api/exchanges/<int:exchange_id>/', ExchangeView.as_view(), name='exchange-detail'),
    path('api/favorites/', FavoritesView.as_view(), name='favorites'),
    path('api/reviews/', UserReviewView.as_view(), name='user-reviews'),
    path('api/addresses/', ShippingAddressView.as_view(), name='shipping-addresses'),
    # Добавьте URL-маршруты для остальных вьюшек
    # ...
]


urlpatterns = [
    path('admin/', admin.site.urls),
]
