from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "publication_year", "availability_status")
    list_filter = ("author", "publisher", "publication_year", "availability_status")
    search_fields = ("title", "author", "publisher", "description")
    ordering = ("publication_year",)
    fieldsets = (
        (None, {
            "fields": ("title", "author", "publisher", "publication_year", "availability_status")
        }),
        ("Description", {
            "fields": ("description", "cover_image", "format", "isbn", "rating", "page_count", "language")
        }),
        ("Pricing", {
            "fields": ("selling_price", "rental_price")
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("title", "author", "publisher", "publication_year", "availability_status",
                       "description", "cover_image", "format", "isbn", "rating", "page_count", "language",
                       "selling_price", "rental_price")
        }),
    )
