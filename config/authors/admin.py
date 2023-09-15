from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "biography")
    list_filter = ("name",)
    search_fields = ("name", "biography")
    ordering = ("name",)
