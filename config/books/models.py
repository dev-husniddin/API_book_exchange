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

    def __str__(self):
        return self.title
