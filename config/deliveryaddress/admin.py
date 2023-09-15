from django.contrib import admin
from .models import ShippingAddress

@admin.register(ShippingAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ("user_id", "address_line1", "city", "state", "postal_code")
    list_filter = ("city", "state")
    search_fields = ("user_id__username", "address_line1", "city", "state", "postal_code")
    ordering = ("user_id",)
