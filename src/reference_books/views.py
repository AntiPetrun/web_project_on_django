from django.shortcuts import render
from . import models


def index(request):
    book_obj = models.Book.objects.all()
    genres = models.LiteraryGenre.objects.all()
    context = {'book_obj': book_obj, 'genres': genres}
    return render(request, 'reference_books/index.html', context)


def by_genre(request, genre_id):
    book_obj = models.Book.objects.filter(genre=genre_id)
    genres = models.LiteraryGenre.objects.all()
    current_genre = models.LiteraryGenre.objects.get(pk=genre_id)
    context = {'book_obj': book_obj, 'genres': genres, 'current_genre': current_genre}
    return render(request, 'reference_books/by_genre.html', context)
