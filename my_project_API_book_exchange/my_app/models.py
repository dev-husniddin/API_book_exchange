from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    description = models.TextField()
    cover_image = models.CharField(max_length=255)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    format = models.CharField(max_length=50)
    availability_status = models.BooleanField()
    isbn = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    page_count = models.IntegerField()
    language = models.CharField(max_length=50)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=255)
    bio = models.TextField()
    preferences = models.JSONField()
    registration_date = models.DateTimeField()
    activation_status = models.BooleanField()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=20)
    quantity = models.IntegerField()
    delivery_address_id = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, null=True)

class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    book_offered_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='offered_exchanges')
    book_requested_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='requested_exchanges')
    user_offering_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offering_exchanges')
    user_requesting_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requesting_exchanges')
    exchange_status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

class Audiobook(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    audio_file = models.CharField(max_length=255)
    duration = models.TimeField()

class Ebook(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    file = models.CharField(max_length=255)

class UserReview(models.Model):
    id = models.AutoField(primary_key=True)
    user_reviewed_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewed_reviews')
    user_reviewer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_reviews')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()

class ShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

class CategoryBook(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

class BookAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

class UserExchange(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    exchange_id = models.ForeignKey(Exchange, on_delete=models.CASCADE)
