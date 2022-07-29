from django.forms import ModelForm
from .models import Book, BookSeria


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookSeriaForm(ModelForm):
    class Meta:
        model = BookSeria
        fields = '__all__'
