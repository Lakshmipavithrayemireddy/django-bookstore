# Create your views here.
# store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Built-in forms
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages # For showing feedback to users
from django.contrib.auth.decorators import login_required # To protect views
from .models import Book

# --- Book Views ---

def book_list(request):
    """Displays the list of all available books."""
    books = Book.objects.filter(stock__gt=0) # Get books with stock > 0
    context = {'books': books}
    return render(request, 'store/book_list.html', context)

def book_detail(request, pk):
    """Displays details for a single book."""
    book = get_object_or_404(Book, pk=pk) # Get book or return 404 error
    context = {'book': book}
    return render(request, 'store/book_detail.html', context)

# --- Cart Views ---

def add_to_cart(request, book_id):
    """Adds a book to the session-based shopping cart."""
    book = get_object_or_404(Book, id=book_id)
    # Initialize cart in session if it doesn't exist
    cart = request.session.get('cart', {})

    # Get current quantity or default to 0, then increment
    current_quantity = cart.get(str(book_id), 0) # Use string keys for session
    # Basic check: Don't add more than available stock (can be improved)
    if current_quantity < book.stock:
         cart[str(book_id)] = current_quantity + 1
         request.session['cart'] = cart # Save cart back to session
         messages.success(request, f"Added '{book.title}' to your cart.")
    else:
         messages.warning(request, f"Sorry, only {book.stock} copies of '{book.title}' available.")

    # Redirect back to the book list or previous page
    # return redirect('store:book_list')
    # Or redirect back to where the user came from (more user-friendly)
    return redirect(request.META.get('HTTP_REFERER', 'store:book_list'))


def view_cart(request):
    """Displays the contents of the shopping cart."""
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for book_id, quantity in cart.items():
        try:
            book = Book.objects.get(id=int(book_id))
            item_total = book.price * quantity
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'item_total': item_total,
            })
            total_price += item_total
        except Book.DoesNotExist:
            # Handle cases where a book might have been deleted
            # Optionally remove it from the cart here
            pass

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/cart.html', context)

# --- Authentication Views ---

def register(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the new user
            login(request, user) # Log the user in immediately
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('store:book_list') # Redirect to home page
        else:
             messages.error(request, "Registration failed. Please correct the errors below.")
    else: # GET request
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

# Note: Login and Logout views are typically handled by django.contrib.auth.urls
# We don't need to write custom views for them unless we want specific customization.
# We just need to provide the templates (see Part 8).