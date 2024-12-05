from django.core.management.base import BaseCommand
from book_manager.models import Book, Author
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Restore the database to the default state with 5 famous books and their authors'

    def handle(self, *args, **kwargs):
        # Delete all books and authors
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Get the admin user (or create one if it doesn't exist)
        admin_user, created = User.objects.get_or_create(
            username="admin",
            defaults={"is_staff": True, "is_superuser": True, "email": "admin@example.com"}
        )
        if created:
            admin_user.set_password("admin")  # Set a default password
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Admin user created with username 'admin' and password 'admin'."))

        # Add famous authors
        authors = {
            "J.K. Rowling": "Author of the Harry Potter series.",
            "George Orwell": "Author of 1984 and Animal Farm.",
            "Harper Lee": "Author of To Kill a Mockingbird.",
            "F. Scott Fitzgerald": "Author of The Great Gatsby.",
            "J.R.R. Tolkien": "Author of The Lord of the Rings.",
            "Jane Austen": "Author of Pride and Prejudice and other classic novels of manners.",
            "Miguel de Cervantes": "Author of Don Quixote, considered the first modern novel.",
        }

        author_objects = {}
        for name, bio in authors.items():
            author_objects[name] = Author.objects.create(name=name, bio=bio, created_by=admin_user)

        # Add famous books with image placeholders
        books = [
            {
                "title": "Harry Potter and the Sorcerer's Stone",
                "author": author_objects["J.K. Rowling"],
                "description": "The first book in the Harry Potter series introduces us to Harry, a young wizard, and his adventures at Hogwarts.",
                "published_date": "1997-06-26",
                "cover_image": "https://cdn.europosters.eu/image/750/telas-harry-potter-philosopher-s-stone-book-cover-i214926.jpg",
                "genre": "Fantasy",
            },
            {
                "title": "1984",
                "author": author_objects["George Orwell"],
                "description": "A dystopian novel set in a totalitarian society ruled by Big Brother.",
                "published_date": "1949-06-08",
                "cover_image": "https://m.media-amazon.com/images/I/612ADI+BVlL._AC_UF1000,1000_QL80_.jpg",
                "genre": "Dystopian",
            },
            {
                "title": "To Kill a Mockingbird",
                "author": author_objects["Harper Lee"],
                "description": "A novel about racial injustice in the Deep South, seen through the eyes of young Scout Finch.",
                "published_date": "1960-07-11",
                "cover_image": "https://cdn.kobo.com/book-images/4e1af857-e0e8-45fa-8922-e4bff584beca/1200/1200/False/to-kill-a-mockingbird-4.jpg",
                "genre": "Fiction",
            },
            {
                "title": "The Great Gatsby",
                "author": author_objects["F. Scott Fitzgerald"],
                "description": "A tragic love story set in the roaring 1920s, focusing on Jay Gatsby's obsession with Daisy Buchanan.",
                "published_date": "1925-04-10",
                "cover_image": "https://cdn.kobo.com/book-images/5addc4c9-fbc1-42d7-a79f-cec7619d4b23/1200/1200/False/the-great-gatsby-a-novel-1.jpg",
                "genre": "Fiction",
            },
            {
                "title": "The Hobbit",
                "author": author_objects["J.R.R. Tolkien"],
                "description": "A prelude to The Lord of the Rings, following Bilbo Baggins' journey to reclaim a treasure guarded by Smaug the dragon.",
                "published_date": "1937-09-21",
                "cover_image": "https://m.media-amazon.com/images/I/712cDO7d73L.jpg",
                "genre": "Fantasy",
            },
            {
                "title": "Pride and Prejudice",
                "author": author_objects["Jane Austen"],
                "description": "A masterpiece of wit and social commentary following Elizabeth Bennet's journey to love and self-discovery in Georgian era England.",
                "published_date": "1813-01-28",
                "cover_image": "https://m.media-amazon.com/images/I/71Q1tPupKjL._AC_UF1000,1000_QL80_.jpg",
                "genre": "Romance",
            },
            {
                "title": "Don Quixote",
                "author": author_objects["Miguel de Cervantes"],
                "description": "The story of an elderly man who, driven mad by reading too many chivalric romances, decides to become a knight-errant.",
                "published_date": "1605-01-16",
                "cover_image": "https://i.harperapps.com/covers/9780062391667/y648.jpg",
                "genre": "Fiction",
            },
        ]

        for book_data in books:
            Book.objects.create(
                title=book_data["title"],
                author=book_data["author"],
                description=book_data["description"],
                published_date=book_data["published_date"],
                cover_image=book_data["cover_image"],
                genre=book_data["genre"],
                user=admin_user,
            )

        self.stdout.write(self.style.SUCCESS("Database restored with 5 famous books."))
