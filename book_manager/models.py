from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Model to represent books."""
    GENRES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Science Fiction', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Biography', 'Biography'),
        ('History', 'History'),
        ('Poetry', 'Poetry'),
        ('Self-Help', 'Self-Help'),
    ]

    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_books")
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    description = models.TextField(blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True, choices=GENRES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def is_liked(self, user):
        """Check if the book is liked by the given user."""
        if user.is_authenticated:
            return self.likes.filter(user=user).exists()
        return False

    def status(self, user):
        """Get the reading status for a specific user."""
        if not user.is_authenticated:
            return None
        try:
            reading_list_entry = self.reading_lists.get(user=user)
            return reading_list_entry.status
        except ReadingList.DoesNotExist:
            return None


class Comment(models.Model):
    """Model to represent comments on books."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

class Like(models.Model):
    """Model to represent likes on books."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.book.title}"

class ReadingList(models.Model):
    """Model to represent a user's reading list."""
    STATUS_CHOICES = (
        ("to_read", "To Read"),
        ("reading", "Reading"),
        ("finished", "Finished"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reading_list")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reading_lists")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="to_read")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")  # Prevent duplicate entries for the same book in the same user's list

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"