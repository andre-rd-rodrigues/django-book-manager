from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("books", views.books_page, name="books_page"),
    path('books/new', views.add_book_page, name='add_book_page'),
    path("books/like", views.like_book, name="like_book"),
    path("books/<int:book_id>", views.book_page, name="book_page"),
    path("books/<int:book_id>/edit", views.edit_book_page, name="edit_book_page"),
    path("books/<int:book_id>/delete", views.delete_book, name="delete_book"),
]
