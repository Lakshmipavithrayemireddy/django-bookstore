# bookstore_project/urls.py
from django.contrib import admin
# *** Make sure 'include' is imported here! ***
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # *** CORRECT LINE FOR THE ROOT URL ***
    path('', include('store.urls', namespace='store')),

    # This line includes Django's built-in login/logout URLs under /accounts/
    path('accounts/', include('django.contrib.auth.urls')),
]