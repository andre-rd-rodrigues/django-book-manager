import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Book, Like, ReadingList, Author
from .forms import BookForm
from django.contrib import messages

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

def books_page(request):
    books = Book.objects.all()
    paginator = Paginator(books, 6)  # Show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Add is_liked status for each book if user is authenticated
    if request.user.is_authenticated:
        for book in page_obj:
            book.is_liked_by_user = book.is_liked(request.user)
            book.status = book.status(request.user)
            book.in_reading_list = book.reading_lists.filter(user=request.user).exists()
    return render(request, 'book_manager/books.html', {'books': page_obj})

@login_required
def book_page(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_manager/book.html', {'book': book})

@login_required
def add_book_page(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New book was added successfully!')
            return redirect('books_page')
        else:
            return render(request, 'book_manager/add_book.html', {'form': form})
    form = BookForm()
    return render(request, 'book_manager/add_book.html', {'form': form})

@login_required
def edit_book_page(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    

    # Check if current user is the creator of the book
    if request.user != book.user:
        messages.error(request, 'You can only edit books that you created.')
        return redirect('books_page')

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book was edited successfully!')
            return redirect('books_page')
        else:
            return render(request, 'book_manager/edit_book.html', {'form': form})
    form = BookForm(instance=book)     
    return render(request, 'book_manager/edit_book.html', {'form': form})

@login_required
def reading_list_page(request):
    reading_list_entries = ReadingList.objects.filter(user=request.user)
    paginator = Paginator(reading_list_entries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Prepare books with additional attributes
    books_with_status = []
    for entry in page_obj:
        book = entry.book
        book.status = entry.status
        book.in_reading_list = True
        books_with_status.append(book)
    
    return render(request, 'book_manager/reading_list.html', {'books': books_with_status, 'page_obj': page_obj})

def authors_page(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    
    return render(request, 'book_manager/authors.html', {'authors': page_obj})

@login_required
def add_author_page(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_page')

@login_required
def edit_author_page(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'book_manager/edit_author.html', {'author': author})

""" API """
@login_required
def like_book(request):
    if request.method == "POST":
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
        return JsonResponse({"liked": liked, "like_count": like_count})
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user != book.user:
        messages.error(request, 'You can only delete books that you created.')
        return redirect('books_page')
    book.delete()
    return redirect('books_page')

@login_required
def manage_reading_list(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, id=book_id)
        data = json.loads(request.body)

        # Handle bookmark icon (home page)
        if "action" in data and data["action"] == "toggle_bookmark":
            # Check if the book is already in the reading list
            reading_list_entry = ReadingList.objects.filter(user=request.user, book=book).first()
            if reading_list_entry:
                reading_list_entry.delete()  # Remove from reading list
                return JsonResponse({"status": "removed"})
            else:
                ReadingList.objects.create(user=request.user, book=book, status="reading")
                return JsonResponse({"status": "added"})

        # Handle status update (reading page)
        if "status" in data:
            status = data["status"]
            valid_statuses = ["to_read", "reading", "finished"]
            if status not in valid_statuses:
                return JsonResponse({"error": "Invalid status"}, status=400)

            # Update or create a ReadingList entry
            reading_list_entry, created = ReadingList.objects.get_or_create(user=request.user, book=book)
            reading_list_entry.status = status
            reading_list_entry.save()
            return JsonResponse({"status": status})

    return JsonResponse({"error": "Invalid request"}, status=400)
