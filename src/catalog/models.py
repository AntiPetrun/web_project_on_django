from django.db import models
from django.urls import reverse
from reference_books.models import Author, Country, Language, Genre, PublishingHouse, Currency


class BookSeria(models.Model):
    title = models.CharField(max_length= 64, db_index=True)
    image = models.ImageField(blank= True, null= True)
    author = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, null=True, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, null=True, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book seria")
    publishing_house = models.ForeignKey(PublishingHouse, null=True, on_delete=models.PROTECT)
    release_date = models.DateField(blank= True, null= True)
    summary = models.TextField(max_length= 2048, blank= True, null= True, help_text="Enter a brief description of the book")
       
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Book Series'
        ordering = ['title']


class Book(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    seria = models.ForeignKey(BookSeria, on_delete=models.PROTECT)
    release_number = models.CharField(max_length=16)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.PROTECT)
    release_date = models.DateField(blank=True, null=True)
    page = models.IntegerField()
    isbn = models.CharField(verbose_name='ISBN', max_length=16, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    price = models.FloatField(max_length=8)
    currency = models.ForeignKey(Currency ,on_delete=models.PROTECT)
    summary = models.TextField(max_length= 2048, blank=True, null=True, help_text="Enter a brief description of the book")
    
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title

    class Meta():
        ordering = ['title']
