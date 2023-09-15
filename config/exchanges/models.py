from django.db import models
from .models import Book  # Импортируйте модель Book
from django.contrib.auth.models import User  # Импортируйте модель User

class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    book_offered_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='offered_books')
    book_requested_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='requested_books')
    user_offering_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offering_users')
    user_requesting_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requesting_users')
    exchange_status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Exchange #{self.id}"
