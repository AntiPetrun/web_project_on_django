from django.contrib import admin
from . import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol')
    list_display_links = ('name', 'code', 'symbol')
    search_fields = ('name', 'code', 'symbol')
    fields = [('name', 'code', 'symbol'),]


class BooksInline(admin.TabularInline):
    model = models.Book


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country_of_birth', 'date_of_birth', 'date_of_death', 'biography',)
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    fields = [('first_name', 'last_name'), 'country_of_birth', ('date_of_birth', 'date_of_death'), 'biography',]
    inlines = [BooksInline]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(models.PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'founding_date', 'country', 'address', 'web_site')
    search_fields = ('name',)


@admin.register(models.BookSeria)
class BookSeriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'country', 'language', 'display_genre', 'publishing_house', 'release_date',)
    search_fields = ('title', 'author', 'display_genre',)
    inlines = [BooksInline]
    fieldsets = (
        (None, {
            'fields': ('display_genre',)
        }),
    )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'country', 'language', 'seria', 'release_number', 'display_genre', 'publishing_house', 'release_date', 'page', 'isbn', 'price', 'currency',)
    search_fields = ('title', 'author', 'display_genre')


admin.site.register(models.Country)
admin.site.register(models.Language)
