from django.contrib import admin
from . import models

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol')
    list_display_links = ('name', 'code', 'symbol')
    search_fields = ('name', 'code', 'symbol')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country_of_birth', 'date_of_birth', 'date_of_death', 'biography',)
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description')

class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'founding_date', 'country', 'address', 'web_site')
    search_fields = ('name',)

class BookSeriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'language', 'genre', 'publishing_house', 'release_date',)
    search_fields = ('title', 'genre',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'language', 'seria', 'release_number', 'display_genre', 'publishing_house', 'release_date', 'page', 'isbn', 'price', 'currency',)
    search_fields = ('title', 'genre')

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.BookSeria, BookSeriaAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.Country)
admin.site.register(models.Language)

