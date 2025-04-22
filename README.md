# Django Online Bookstore

A simple web application simulating an online bookstore built using the Python Django framework. This project demonstrates core Django concepts including models, views, templates, URL routing, user authentication, session management, and the Django Admin interface.

## Features

*   **Book Catalog:** Displays a list of available books fetched from the database.
*   **Book Details:** Shows detailed information for each book (author, description, price, stock).
*   **User Authentication:** Secure user registration, login, and logout functionality using Django's built-in authentication system.
*   **Shopping Cart:** Session-based shopping cart allowing logged-in users to:
    *   Add books to the cart.
    *   View items currently in the cart with quantity and total price.
*   **Admin Interface:** Basic Django Admin integration for managing Book records (adding, editing, deleting).

## Technology Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Django Templates
*   **Database:** SQLite (Default Django database)
*   **Version Control:** Git / GitHub

## Setup and Installation

Follow these steps to set up the project locally:

1.  **Prerequisites:**
    *   Python 3.x installed
    *   pip (Python package installer) installed
    *   Git installed

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Lakshmipavithrayemireddy/django-bookstore.git
    cd django-bookstore
    ```
  

3.  **Create and Activate Virtual Environment:**
    *   It's highly recommended to use a virtual environment:
    ```bash
    python -m venv venv
    ```
    *   Activate the environment:
        *   Windows: `.\venv\Scripts\activate`
        *   macOS/Linux: `source venv/bin/activate`

4.  **Install Dependencies:**
    *   Install Django (the primary dependency):
    ```bash
    pip install django
    ```
   
5.  **Apply Database Migrations:**
    *   Set up the database schema based on the models defined:
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (for Admin Access):**
    *   Create an admin account to manage books:
    ```bash
    python manage.py createsuperuser
    ```
    *   Follow the prompts to set a username, email (optional), and password.

7.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    *   The application should now be running at `http://127.0.0.1:8000/`

## Usage

1.  **Admin Panel:**
    *   Navigate to `http://127.0.0.1:8000/admin/`
    *   Log in using the superuser credentials created earlier.
    *   Go to the "Store" section -> "Books".
    *   Click "+ Add book" to add new books with their details (title, author, price, stock, optional description/image URL).

2.  **Main Site:**
    *   Navigate to `http://127.0.0.1:8000/`
    *   Browse the available books.
    *   Click on a book title to view details.
    *   Use the "Register" link to create a new user account.
    *   Use the "Login" link to log in.
    *   While logged in, click "Add to Cart" on book list or detail pages.
    *   Click "View Cart" to see the items added.
    *   Click "Logout" to end the session.

