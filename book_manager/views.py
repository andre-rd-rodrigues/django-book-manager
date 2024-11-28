import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Book, Like

def index(request):
    return render(request, "book_manager/index.html")

""" Authentication views """
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "book_manager/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "book_manager/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "book_manager/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "book_manager/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "book_manager/register.html")

""" Books Page """
def books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)  # Show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Add is_liked status for each book if user is authenticated
    if request.user.is_authenticated:
        for book in page_obj:
            book.is_liked_by_user = book.is_liked(request.user)

    return render(request, 'book_manager/books.html', {'books': page_obj})

""" Book Page """
def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_manager/book.html', {'book': book})

""" Add Book Page """
def add_book(request):
    return render(request, 'book_manager/add_book.html')

""" API """
def like_book(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        book_id = data.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        # Check if the user already liked this book
        existing_like = Like.objects.filter(book=book, user=request.user)
        if existing_like.exists():
            # Unlike the book if it was already liked
            existing_like.delete()
            liked = False
        else:
            # Add a new like
            Like.objects.create(book=book, user=request.user)
            liked = True

        # Return the updated like count
        like_count = book.likes.count()
        print(like_count, liked)
        return JsonResponse({"liked": liked, "like_count": like_count})
    return JsonResponse({"error": "Invalid request"}, status=400)