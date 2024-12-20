from django import forms
from .models import Book, Author, Rating

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date', 'description', 'cover_image']
      
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a description'}),
            'cover_image': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/book-cover.jpg'}),
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'genre': 'Genre',
            'published_date': 'Publication Date',
            'description': 'Description',
            'cover_image': 'Image URL',
        }

    def clean_title(self):
        """Ensure the book title is unique."""
        title = self.cleaned_data.get('title')
        if Book.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("A book with this title already exists.")
        return title

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']
        labels = {
            'name': 'Name',
            'bio': 'Biography',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the author name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a bio'}),
        }

    def clean_name(self):
        """Ensure the author name is unique."""
        name = self.cleaned_data.get('name')
        if Author.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("An author with this name already exists.")
        return name

class RatingForm(forms.ModelForm):
    class Meta:
        RATING_CHOICES =[
            (5, '5 - Excellent'),
            (4, '4 - Very Good'),
            (3, '3 - Good'),
            (2, '2 - Fair'),
            (1, '1 - Poor'),
        ]
        model = Rating
        fields = ['rating', 'comment']

        labels = {
            'rating': 'Rating',
            'comment': 'Comment',
        }

        widgets = {
            'rating': forms.Select(choices=RATING_CHOICES, attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a comment'}),
        }
