from multiprocessing.context import ForkProcess
from pyexpat import model
from django.contrib import admin
from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'first_name', 'last_name', 'country_birth', 'date_birth', 'biography')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'first_name', 'last_name', 'biography')


class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_name', 'image', 'country', 'language', 'genre', 'publishing_house', 'release_date', 'description')
    list_display_links = ('name', 'original_name')
    search_fields = ('name', 'original_name', 'description')


class LiteraryGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description')


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founding_date', 'address', 'web_site')
    list_display_links = ('name',)
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_name', 'image', 'country', 'language', 'seria', 'release_number','genre', 'publishing_house', 'release_date', 'page', 'isbn', 'price', 'currency', 'description')
    list_display_links = ('name', 'original_name')
    search_fields = ('name', 'original_name', 'description')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol')
    list_display_links = ('name', 'code', 'symbol')
    search_fields = ('name', 'code', 'symbol')


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.BookSeries, BookSeriesAdmin)
admin.site.register(models.LiteraryGenre, LiteraryGenreAdmin)
admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.Country)
admin.site.register(models.Language)
