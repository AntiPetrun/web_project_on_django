from django.shortcuts import render
from . import models
from django.views.generic.edit import CreateView
from .forms import ReferenceBookForm
from django.urls import reverse_lazy


def index(request):
    book_obj = models.Book.objects.all()
    genres = models.Genre.objects.all()
    context = {'book_obj': book_obj, 'genres': genres}
    return render(request, 'reference_books/index.html', context)


def by_genre(request, genre_id):
    book_obj = models.Book.objects.filter(genre=genre_id)
    genres = models.Genre.objects.all()
    current_genre = models.Genre.objects.get(pk=genre_id)
    context = {'book_obj': book_obj, 'genres': genres, 'current_genre': current_genre}
    return render(request, 'reference_books/by_genre.html', context)


class ReferenceBookCreateView(CreateView):
    template_name = 'reference_books/create.html'
    form_class = ReferenceBookForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = models.Author.objects.all()
        context['country'] = models.Country.objects.all()
        context['language'] = models.Language.objects.all()
        context['seria'] = models.BookSeria.objects.all()
        context['genre'] = models.Genre.objects.all()
        context['publishing_house'] = models.PublishingHouse.objects.all()
        context['currency'] = models.Currency.objects.all()
        return context
