from catalog import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import BookForm, BookSeriaForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(generic.ListView):
    template_name = 'catalog/books.html'
    model = models.Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'catalog/edit-book.html'
#    login_url = reverse_lazy('login')
#    redirect_field_name = 'next'
    model = models.Book
    form_class = BookForm
    
    def get_success_url(self):
        return reverse_lazy('book-detail', args = (self.object.id,))


class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'catalog/delete-book.html'
    model = models.Book
    success_url = reverse_lazy('books')


class BookDetailView(generic.DetailView):
    template_name = 'catalog/book-detail.html'
    model = models.Book
    

class BookCreateView(LoginRequiredMixin, CreateView):
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


class BookSeriaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'catalog/add-book-seria.html'
    form_class = BookSeriaForm
    success_url = reverse_lazy('homepage')
    
        
    def get_success_url(self):
        return reverse_lazy('book-seria-detail', args = (self.object.id,))
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = models.Author.objects.all()
        context['country'] = models.Country.objects.all()
        context['language'] = models.Language.objects.all()
        context['genre'] = models.Genre.objects.all()
        context['publishing_house'] = models.PublishingHouse.objects.all()
        return context


class BookSeriaDetailView(generic.DetailView):
    template_name = 'catalog/book-seria-detail.html'
    model = models.BookSeria


class BookSeriaListView(generic.ListView):
    template_name = 'catalog/book-series.html'
    model = models.BookSeria


class BookSeriaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'catalog/edit-book-seria.html'
    model = models.BookSeria
    form_class = BookSeriaForm
    
    def get_success_url(self):
        return reverse_lazy('book-seria-detail', args = (self.object.id,))


class BookSeriaDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'catalog/delete-book-seria.html'
    model = models.BookSeria
    success_url = reverse_lazy('homepage')
