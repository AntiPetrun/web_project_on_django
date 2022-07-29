from django.shortcuts import render
from reference_books.models import Genre
from catalog.models import Book


def by_genre(request, genre_id):
    book_obj = Book.objects.filter(genre=genre_id)
    genres = Genre.objects.all()
    current_genre = Genre.objects.get(pk=genre_id)
    context = {'book_obj': book_obj, 'genres': genres, 'current_genre': current_genre}
    return render(request, 'reference_books/by_genre.html', context)
