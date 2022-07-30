from django.shortcuts import render
from catalog.models import Book
from reference_books.models import Genre


def index(request):
    book_list = Book.objects.all()
    genres = Genre.objects.all()
    context = {'book_list': book_list, 'genres': genres}
    return render(request, 'homepage/index.html', context)
