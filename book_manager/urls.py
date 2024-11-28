from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("books", views.books, name="books"),
    path("book/<int:book_id>", views.book, name="book"),
    
    path("books/like", views.like_book, name="like_book"),
]
