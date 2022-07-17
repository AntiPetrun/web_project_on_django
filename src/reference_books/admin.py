from multiprocessing.context import ForkProcess
from pyexpat import model
from django.contrib import admin
from .models import Author, BookSeries, LiteraryGenre, PublishingHouse, Country, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'first_name', 'last_name', 'country_birth', 'date_birth', 'biography')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'first_name', 'last_name', 'biography')


class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_name', 'genre', 'country', 'language', 'publish_house', 'release_date', 'rus_release_date', 'image')
    list_display_links = ('name', 'original_name')
    search_fields = ('name', 'original_name', 'genre', 'country')


class LiteraryGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description')


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founding_date', 'address', 'web_site')
    list_display_links = ('name',)
    search_fields = ('name', 'country')


admin.site.register(Author, AuthorAdmin)
admin.site.register(BookSeries, BookSeriesAdmin)
admin.site.register(LiteraryGenre, LiteraryGenreAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Country)
admin.site.register(Language)
