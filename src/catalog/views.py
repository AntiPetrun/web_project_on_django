from catalog import models
from django.views.generic.edit import CreateView
from .forms import BookForm, BookSeriaForm
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    template_name = 'catalog/create-book.html'
    form_class = BookForm
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

class BookSeriaCreateView(CreateView):
    template_name = 'catalog/create-book-seria.html'
    form_class = BookSeriaForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = models.Author.objects.all()
        context['country'] = models.Country.objects.all()
        context['language'] = models.Language.objects.all()
        context['genre'] = models.Genre.objects.all()
        context['publishing_house'] = models.PublishingHouse.objects.all()
        return context
