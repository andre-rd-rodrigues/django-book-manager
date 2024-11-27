from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                 # Homepage of the app
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
    # path('books/', views.book_list, name='book_list'),   # List of all books
    # path('books/<int:pk>/', views.book_detail, name='book_detail'),  # Book detail view
    # path('authors/', views.author_list, name='author_list'),  # List of authors
]
