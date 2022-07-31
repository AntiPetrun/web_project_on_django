from catalog import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import BookForm, BookSeriaForm
from django.urls import reverse_lazy
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'catalog/books.html'
    model = models.Book


class BookUpdateView(UpdateView):
    template_name = 'catalog/edit-book.html'
    model = models.Book


class BookDeleteView(DeleteView):
    template_name = 'catalog/delete-book.html'
    model = models.Book
    success_url = reverse_lazy('index')


class BookDetailView(generic.DetailView):
    template_name = 'catalog/book-detail.html'
    model = models.Book
    

class BookCreateView(CreateView):
    template_name = 'catalog/add-book.html'
    form_class = BookForm
    
    def get_success_url(self):
        return reverse_lazy('book-detail', args = (self.object.id,))
    
    
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
    template_name = 'catalog/add-seria.html'
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
