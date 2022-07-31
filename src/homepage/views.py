from django.shortcuts import render
from catalog.models import Book
from reference_books.models import Genre, Author


def index(request):
    book_list = Book.objects.all()
    genres = Genre.objects.all()
    context = {'book_list': book_list, 'genres': genres}
    return render(request, 'homepage/index.html', context)


def by_genre(request, genre_id):
    book_list = Book.objects.filter(genre=genre_id)
    genres = Genre.objects.all()
    current_genre = Genre.objects.get(pk=genre_id)
    context = {'book_list': book_list, 'genres': genres, 'current_genre': current_genre}
    return render(request, 'homepage/by_genre.html', context)


def by_author(request, author_id):
    book_list = Book.objects.filter(pk=author_id)
    authors = Author.objects.all()
    current_author = Author.objects.get(pk=author_id)
    context = {'book_list': book_list, 'authors': authors, 'current_author': current_author}
    return render(request, 'homepage/by_author.html', context)
