from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("book_id", "user_id", "order_type", "order_status", "quantity", "order_date")
    list_filter = ("order_type", "order_status")
    search_fields = ("book_id__title", "user_id__username", "order_type", "order_status")
    ordering = ("order_date",)
