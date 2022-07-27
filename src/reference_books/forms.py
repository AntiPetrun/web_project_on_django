from django.forms import ModelForm
from . import models


class ReferenceBookForm(ModelForm):
    class Meta:
        model = models.Book
        fields = ('title', 'image', 'release_number', 'release_date', 'page', 'isbn', 'price', 'summary')
