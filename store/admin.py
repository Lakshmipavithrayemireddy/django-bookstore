from django.contrib import admin

# Register your models here.
# store/admin.py
from .models import Book

# Simple registration
admin.site.register(Book)

# Optional: Customize how Books are displayed in the admin
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price', 'stock')
#     search_fields = ('title', 'author')
#
# admin.site.register(Book, BookAdmin) # Use this line instead of the simple one above
