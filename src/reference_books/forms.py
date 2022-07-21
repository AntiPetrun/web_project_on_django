from django.forms import ModelForm
from . import models


class ReferenceBookForm(ModelForm):
    class Meta:
        model = models.Book
        fields = ('name', 'original_name', 'image', 'country', 'language', 'seria', 'release_number','genre', 'publishing_house', 'release_date', 'page', 'isbn', 'price', 'currency', 'description')
