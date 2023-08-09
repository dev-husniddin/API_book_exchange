from django.shortcuts import render
from django.views import View
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View

class UserRegistrationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        return JsonResponse(data={"status": "User registered", "user_id": user.id})

class UserLoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.get(username=username)
        if user.check_password(password):
            return JsonResponse(data={"status": "Login successful", "user_id": user.id})
        else:
            return JsonResponse(data={"error": "Invalid credentials"})

class UserProfileView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        if user:
            user_data = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "profile_image": user.profile_image.url if user.profile_image else None,
                "bio": user.bio,
                "preferences": user.preferences,
                "registration_date": user.date_joined,
                "activation_status": user.is_active
            }
            return JsonResponse(data=user_data)
        else:
            return JsonResponse(data={"error": "User not found"})

# Продолжайте создавать аналогичные вьюшки для остальных моделей и функций, описанных в ТЗ
# ...

# Примеры ваших других вьюшек


class BookView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        if book:
            book_data = {
                "title": book.title,
                "author": book.author,
                "publisher": book.publisher,
                "publication_year": book.publication_year,
                "description": book.description,
                "cover_image": book.cover_image,
                "selling_price": book.selling_price,
                "rental_price": book.rental_price,
                "format": book.format,
                "availability_status": book.availability_status,
                "isbn": book.isbn,
                "rating": book.rating,
                "page_count": book.page_count,
                "language": book.language
            }
            return JsonResponse(data=book_data)
        else:
            return JsonResponse(data={"error": "Book not found"})

class CategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        if category:
            category_data = {
                "name": category.name,
                "description": category.description
            }
            return JsonResponse(data=category_data)
        else:
            return JsonResponse(data={"error": "Category not found"})

class AuthorView(View):
    def get(self, request, author_id):
        author = Author.objects.get(pk=author_id)
        if author:
            author_data = {
                "name": author.name,
                "biography": author.biography
            }
            return JsonResponse(data=author_data)
        else:
            return JsonResponse(data={"error": "Author not found"})

class OrderView(View):
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        if order:
            order_data = {
                "book_id": order.book.id,
                "user_id": order.user.id,
                "order_type": order.order_type,
                "order_date": order.order_date,
                "order_status": order.order_status,
                "quantity": order.quantity,
                "delivery_address_id": order.delivery_address.id
            }
            return JsonResponse(data=order_data)
        else:
            return JsonResponse(data={"error": "Order not found"})

class ExchangeView(View):
    def get(self, request, exchange_id):
        exchange = Exchange.objects.get(pk=exchange_id)
        if exchange:
            exchange_data = {
                "book_offered_id": exchange.book_offered.id,
                "book_requested_id": exchange.book_requested.id,
                "user_offering_id": exchange.user_offering.id,
                "user_requesting_id": exchange.user_requesting.id,
                "exchange_status": exchange.exchange_status,
                "start_date": exchange.start_date,
                "end_date": exchange.end_date
            }
            return JsonResponse(data=exchange_data)
        else:
            return JsonResponse(data={"error": "Exchange not found"})

class FavoritesView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        if user:
            favorites = Favorites.objects.filter(user=user)
            favorites_data = []
            for fav in favorites:
                favorites_data.append({
                    "user_id": fav.user.id,
                    "book_id": fav.book.id
                })
            return JsonResponse(data={"favorites": favorites_data})
        else:
            return JsonResponse(data={"error": "User not found"})

class UserReviewView(View):
    def get(self, request, review_id):
        review = UserReview.objects.get(pk=review_id)
        if review:
            review_data = {
                "user_reviewed_id": review.user_reviewed.id,
                "user_reviewer_id": review.user_reviewer.id,
                "rating": review.rating,
                "comment": review.comment
            }
            return JsonResponse(data=review_data)
        else:
            return JsonResponse(data={"error": "Review not found"})

class ShippingAddressView(View):
    def get(self, request, address_id):
        address = ShippingAddress.objects.get(pk=address_id)
        if address:
            address_data = {
                "user_id": address.user.id,
                "address_line1": address.address_line1,
                "address_line2": address.address_line2,
                "city": address.city,
                "state": address.state,
                "country": address.country,
                "postal_code": address.postal_code
            }
            return JsonResponse(data=address_data)
        else:
            return JsonResponse(data={"error": "Address not found"})

