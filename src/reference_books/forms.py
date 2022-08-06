from django.forms import ModelForm
from .models import Author, Currency, Genre, Country, Language, PublishingHouse


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class PublishingHouseForm(ModelForm):
    class Meta:
        model = PublishingHouse
        fields = '__all__'
