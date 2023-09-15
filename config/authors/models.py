from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name
