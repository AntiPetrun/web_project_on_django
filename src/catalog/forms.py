from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'image', 'release_number', 'release_date', 'page', 'isbn', 'price', 'summary')
