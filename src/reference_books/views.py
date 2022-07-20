from django.shortcuts import render
from . import models


def index(request):
    book_obj = models.Book.objects.all()
    return render(request, 'reference_books/index.html', {'book_obj': book_obj})
