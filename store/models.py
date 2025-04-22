from django.db import models

# Create your models here.
# store/models.py
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True) # Optional description
    price = models.DecimalField(max_digits=6, decimal_places=2) # e.g., 9999.99
    stock = models.PositiveIntegerField(default=0) # Number of books available
    # Using a URLField is simplest for now, assumes images are hosted elsewhere
    cover_image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        # How the object will be displayed in the admin site or shell
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        # Returns the URL to access a detail record for this book.
        return reverse('store:book_detail', args=[str(self.id)])