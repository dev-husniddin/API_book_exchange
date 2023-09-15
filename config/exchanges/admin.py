from django.contrib import admin
from .models import Exchange

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ("book_offered_id", "book_requested_id", "user_offering_id", "user_requesting_id", "exchange_status")
    list_filter = ("exchange_status",)
    search_fields = ("book_offered_id__title", "book_requested_id__title", "user_offering_id__username", "user_requesting_id__username")
    ordering = ("exchange_status",)
