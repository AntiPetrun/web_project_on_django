from multiprocessing.context import ForkProcess
from pyexpat import model
from django.contrib import admin
from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'first_name', 'last_name', 'country_birth', 'date_birth', 'biography')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'first_name', 'last_name', 'biography')


class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_name', 'image', 'country', 'language', 'genre', 'publishing_house', 'release_date', 'rus_release_date')
    list_display_links = ('name', 'original_name')
    search_fields = ('name', 'original_name')


class LiteraryGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description')


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founding_date', 'address', 'web_site')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.BookSeries, BookSeriesAdmin)
admin.site.register(models.LiteraryGenre, LiteraryGenreAdmin)
admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
admin.site.register(models.Country)
admin.site.register(models.Language)
