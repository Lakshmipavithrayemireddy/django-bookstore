# store/urls.py
from django.urls import path
from . import views # Import views from the current directory

app_name = 'store' # Define the namespace

urlpatterns = [
    # Home page - list all books
    path('', views.book_list, name='book_list'),
    # Detail page for a single book
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    # URL to add a book to the cart
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    # URL to view the shopping cart
    path('cart/', views.view_cart, name='view_cart'),
     # URL for user registration
    path('register/', views.register, name='register'),
    # Note: Login and Logout views/URLs are handled by django.contrib.auth.urls included in the main urls.py
]