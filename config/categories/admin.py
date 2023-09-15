from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("name",)
    search_fields = ("name", "description")
    ordering = ("name",)
