from django.shortcuts import render
from catalog.models import Book
from reference_books.models import Genre


def index(request):
    book_obj = Book.objects.all()
    genres = Genre.objects.all()
    context = {'book_obj': book_obj, 'genres': genres}
    return render(request, 'homepage/index.html', context)
