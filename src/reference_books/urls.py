from django.urls import path
from .views import AuthorDetailView, AuthorListView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView
from .views import GenreDetailView, GenreListView, GenreCreateView, GenreDeleteView, GenreUpdateView
from .views import CountryCreateView, CountryDeleteView, CountryDetailView, CountryListView, CountryUpdateView
from .views import LanguageCreateView, LanguageDeleteView, LanguageDetailView, LanguageListView, LanguageUpdateView
from .views import CurrencyCreateView, CurrencyDeleteView, CurrencyDetailView, CurrencyListView, CurrencyUpdateView
from .views import PublishingHouseCreateView, PublishingHouseDeleteView, PublishingHouseDetailView, PublishingHouseListView, PublishingHouseUpdateView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/detail', AuthorDetailView.as_view(), name='author-detail'),
    path('add-author/', AuthorCreateView.as_view(), name='add-author'),
    path('delete-author/<int:pk>/delete', AuthorDeleteView.as_view(), name='delete-author'),
    path('edit-author/<int:pk>/update', AuthorUpdateView.as_view(), name='edit-author'),
]

urlpatterns += [
    path('genres/', GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>/detail', GenreDetailView.as_view(), name='genre-detail'),
    path('add-genre/', GenreCreateView.as_view(), name='add-genre'),
    path('delete-genre/<int:pk>/delete', GenreDeleteView.as_view(), name='delete-genre'),
    path('edit-genre/<int:pk>/update', GenreUpdateView.as_view(), name='edit-genre'),
]

urlpatterns += [
    path('countries/', CountryListView.as_view(), name='countries'),
    path('country/<int:pk>/detail', CountryDetailView.as_view(), name='country-detail'),
    path('add-country/', CountryCreateView.as_view(), name='add-country'),
    path('delete-country/<int:pk>/delete', CountryDeleteView.as_view(), name='delete-country'),
    path('edit-country/<int:pk>/update', CountryUpdateView.as_view(), name='edit-country'),
]

urlpatterns += [
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('language/<int:pk>/detail', LanguageDetailView.as_view(), name='language-detail'),
    path('add-language/', LanguageCreateView.as_view(), name='add-language'),
    path('delete-language/<int:pk>/delete', LanguageDeleteView.as_view(), name='delete-language'),
    path('edit-language/<int:pk>/update', LanguageUpdateView.as_view(), name='edit-language'),
]

urlpatterns += [
    path('currencies/', CurrencyListView.as_view(), name='currencies'),
    path('currency/<int:pk>/detail', CurrencyDetailView.as_view(), name='currency-detail'),
    path('add-currency/', CurrencyCreateView.as_view(), name='add-currency'),
    path('delete-currency/<int:pk>/delete', CurrencyDeleteView.as_view(), name='delete-currency'),
    path('edit-currency/<int:pk>/update', CurrencyUpdateView.as_view(), name='edit-currency'),
]

urlpatterns += [
    path('publishinghouses/', PublishingHouseListView.as_view(), name='publishinghouses'),
    path('publishinghouse/<int:pk>/detail', PublishingHouseDetailView.as_view(), name='publishinghouse-detail'),
    path('add-publishinghouse/', PublishingHouseCreateView.as_view(), name='add-publishinghouse'),
    path('delete-publishinghouse/<int:pk>/delete', PublishingHouseDeleteView.as_view(), name='delete-publishinghouse'),
    path('edit-publishinghouse/<int:pk>/update', PublishingHouseUpdateView.as_view(), name='edit-publishinghouse'),
]
