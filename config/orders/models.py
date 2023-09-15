from django.db import models
from django.core.validators import MinValueValidator  # Импортируйте MinValueValidator
from .models import Book, User, ShippingAddress  # Импортируйте модели Book и User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=20)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])  # Используйте MinValueValidator
    delivery_address_id = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id}"
