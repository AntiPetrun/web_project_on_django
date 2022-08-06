from . import models
from django.views import generic
from .forms import AuthorForm, CountryForm, CurrencyForm, GenreForm, LanguageForm, PublishingHouseForm
from django.urls import reverse_lazy


class AuthorDetailView(generic.DetailView):
    template_name = 'reference_books/author-detail.html'
    model = models.Author


class AuthorListView(generic.ListView):
    template_name = 'reference_books/authors.html'
    model = models.Author


class AuthorCreateView(generic.CreateView):
    template_name = 'reference_books/add-author.html'
    form_class = AuthorForm
    
    def get_success_url(self):
        return reverse_lazy('author-detail', args = (self.object.id,))
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_of_birth'] = models.Country.objects.all()
        return context


class AuthorDeleteView(generic.DeleteView):
    template_name = 'reference_books/delete-author.html'
    model = models.Author
    success_url = reverse_lazy('authors')


class AuthorUpdateView(generic.UpdateView):
    template_name = 'reference_books/edit-author.html'
    model = models.Author
    form_class = AuthorForm
    
    def get_success_url(self):
        return reverse_lazy('author-detail', args = (self.object.id,))


class GenreListView(generic.ListView):
    template_name = 'reference_books/genres.html'
    model = models.Genre


class GenreDetailView(generic.DetailView):
    template_name = 'reference_books/genre-detail.html'
    model = models.Genre


class GenreCreateView(generic.CreateView):
    template_name = 'reference_books/add-genre.html'
    form_class = GenreForm
    
    def get_success_url(self):
        return reverse_lazy('genre-detail', args = (self.object.id,))


class GenreDeleteView(generic.DeleteView):
    template_name = 'reference_books/delete-genre.html'
    model = models.Genre
    success_url = reverse_lazy('genres')


class GenreUpdateView(generic.UpdateView):
    template_name = 'reference_books/edit-genre.html'
    model = models.Genre
    form_class = GenreForm
    
    def get_success_url(self):
        return reverse_lazy('genre-detail', args = (self.object.id,))


class CountryListView(generic.ListView):
    template_name = 'reference_books/countries.html'
    model = models.Country


class CountryDetailView(generic.DetailView):
    template_name = 'reference_books/country-detail.html'
    model = models.Country


class CountryCreateView(generic.CreateView):
    template_name = 'reference_books/add-country.html'
    form_class = CountryForm
    
    def get_success_url(self):
        return reverse_lazy('country-detail', args = (self.object.id,))


class CountryDeleteView(generic.DeleteView):
    template_name = 'reference_books/delete-country.html'
    model = models.Country
    success_url = reverse_lazy('countries')


class CountryUpdateView(generic.UpdateView):
    template_name = 'reference_books/edit-country.html'
    model = models.Country
    form_class = CountryForm
    
    def get_success_url(self):
        return reverse_lazy('country-detail', args = (self.object.id,))


class LanguageListView(generic.ListView):
    template_name = 'reference_books/languages.html'
    model = models.Language


class LanguageDetailView(generic.DetailView):
    template_name = 'reference_books/language-detail.html'
    model = models.Language


class LanguageCreateView(generic.CreateView):
    template_name = 'reference_books/add-language.html'
    form_class = LanguageForm
    
    def get_success_url(self):
        return reverse_lazy('language-detail', args = (self.object.id,))


class LanguageDeleteView(generic.DeleteView):
    template_name = 'reference_books/delete-language.html'
    model = models.Language
    success_url = reverse_lazy('languages')


class LanguageUpdateView(generic.UpdateView):
    template_name = 'reference_books/edit-language.html'
    model = models.Language
    form_class = LanguageForm
    
    def get_success_url(self):
        return reverse_lazy('language-detail', args = (self.object.id,))


class CurrencyListView(generic.ListView):
    template_name = 'reference_books/currencies.html'
    model = models.Currency


class CurrencyDetailView(generic.DetailView):
    template_name = 'reference_books/currency-detail.html'
    model = models.Currency


class CurrencyCreateView(generic.CreateView):
    template_name = 'reference_books/add-currency.html'
    form_class = CurrencyForm
    
    def get_success_url(self):
        return reverse_lazy('currency-detail', args = (self.object.id,))


class CurrencyDeleteView(generic.DeleteView):
    template_name = 'reference_books/delete-currency.html'
    model = models.Currency
    success_url = reverse_lazy('currencies')


class CurrencyUpdateView(generic.UpdateView):
    template_name = 'reference_books/edit-currency.html'
    model = models.Currency
    form_class = CurrencyForm
    
    def get_success_url(self):
        return reverse_lazy('currency-detail', args = (self.object.id,))


class PublishingHouseListView(generic.ListView):
    template_name = 'reference_books/publishinghouses.html'
    model = models.PublishingHouse


class PublishingHouseDetailView(generic.DetailView):
    template_name = 'reference_books/publishinghouse-detail.html'
    model = models.PublishingHouse


class PublishingHouseCreateView(generic.CreateView):
    template_name = 'reference_books/add-publishinghouse.html'
    form_class = PublishingHouseForm
    
    def get_success_url(self):
        return reverse_lazy('publishinghouse-detail', args = (self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = models.Country.objects.all()
        return context


class PublishingHouseDeleteView(generic.DeleteView):
    template_name = 'reference_books/delete-publishinghouse.html'
    model = models.PublishingHouse
    success_url = reverse_lazy('publishinghouses')


class PublishingHouseUpdateView(generic.UpdateView):
    template_name = 'reference_books/edit-publishinghouse.html'
    model = models.PublishingHouse
    form_class = PublishingHouseForm
    
    def get_success_url(self):
        return reverse_lazy('publishinghouse-detail', args = (self.object.id,))
