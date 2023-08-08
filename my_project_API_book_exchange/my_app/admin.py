from django.contrib import admin
from .models import Book, User, Category, Author, Order, Exchange, Favorites, Audiobook, Ebook, UserReview, ShippingAddress, CategoryBook, BookAuthor, UserExchange

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "publisher", "publication_year", "availability_status")
    list_filter = ("availability_status", "publisher")
    search_fields = ("title", "author")
    list_display_links = ("id", "title")
    list_per_page = 10
    # date_hierarchy = "publish_year"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "registration_date", "activation_status")
    list_filter = ("activation_status",)
    search_fields = ("username", "email")
    list_display_links = ("id", "username")
    list_per_page = 10
    # date_hierarchy = "registration_date"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")
    list_per_page = 10

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")
    list_per_page = 10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "book_id", "user_id", "order_type", "order_date", "order_status", "quantity")
    list_filter = ("order_type", "order_status")
    list_display_links = ("id",)
    list_per_page = 10
    # date_hierarchy = "order_date"

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ("id", "book_offered_id", "book_requested_id", "user_offering_id", "user_requesting_id", "exchange_status", "start_date", "end_date")
    list_filter = ("exchange_status",)
    list_display_links = ("id",)
    list_per_page = 10
    # date_hierarchy = "start_date"

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "book_id")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
    list_display = ("id", "book_id", "duration")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ("id", "book_id", "file")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user_reviewed_id", "user_reviewer_id", "rating", "comment")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "city", "state", "country", "postal_code")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ("id", "category_id", "book_id")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "book_id", "author_id")
    list_display_links = ("id",)
    list_per_page = 10

@admin.register(UserExchange)
class UserExchangeAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "exchange_id")
    list_display_links = ("id",)
    list_per_page = 10
