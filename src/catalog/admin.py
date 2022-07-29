from django.contrib import admin
from . import models


class BooksInline(admin.TabularInline):
    model = models.Book


@admin.register(models.BookSeria)
class BookSeriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'country', 'language', 'display_genre', 'publishing_house', 'release_date',)
    search_fields = ('title', 'author', 'display_genre',)
    inlines = [BooksInline]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'country', 'language', 'seria', 'release_number', 'display_genre', 'publishing_house', 'release_date', 'page', 'isbn', 'price', 'currency',)
    search_fields = ('title', 'author', 'display_genre')
