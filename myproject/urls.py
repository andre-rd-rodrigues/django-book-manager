from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),               # Admin site
    path('', include('book_manager.urls')),        # Include URLs from book_manager app
]
