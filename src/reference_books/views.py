from . import models
from django.views import generic

class AuthorDetailView(generic.DetailView):
    template_name = 'reference_books/author-detail.html'
    model = models.Author


class AuthorListView(generic.ListView):
    template_name = 'reference_books/authors.html'
    model = models.Author
