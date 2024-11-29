from django import forms
from .models import Book, Author

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
