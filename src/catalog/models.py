from django.db import models
from django.urls import reverse
from reference_books.models import Author, Country, Language, Genre, PublishingHouse, Currency


class BookSeria(models.Model):
    title = models.CharField(max_length= 64, db_index=True)
    pic = models.ImageField(upload_to ='uploads/% Y/% m/% d/' ,blank= True, null= True)
    author = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, null=True, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, null=True, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book seria")
    publishing_house = models.ManyToManyField(PublishingHouse, help_text="Select a Publishing House for this book")
    release_date = models.DateField(blank= True, null= True)
    summary = models.TextField(max_length= 2048, blank= True, null= True, help_text="Enter a brief description of the book")
       
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    
           
    def display_publishing_house(self):
        return ', '.join([ publishing_house.name for publishing_house in self.publishing_house.all()[:3] ])
    display_publishing_house.short_description = 'Publishing House'
    
    
    def get_absolute_url(self):
        return reverse('book-seria-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Book Series'
        ordering = ['title']


class Book(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    pic = models.ImageField(upload_to ='uploads/% Y/% m/% d/' ,blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    seria = models.ForeignKey(BookSeria, on_delete=models.PROTECT)
    
    RELEASE_NUMBER = (
        ('1', '1st in series'),
        ('2', '2st in series'),
        ('3', '3st in series'),
        ('4', '4st in series'),
        ('5', '5st in series'),
        ('6', '6st in series'),
        ('7', '7st in series'),
        ('8', '8st in series'),
        ('9', '9st in series'),
    )

    release_number = models.CharField(max_length=1, choices=RELEASE_NUMBER, blank=True, default='1', help_text='Book number in the book series')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    publishing_house = models.ManyToManyField(PublishingHouse, help_text="Select a Publishing House for this book")
    release_date = models.DateField(blank=True, null=True)
    page = models.IntegerField()
    isbn = models.CharField(verbose_name='ISBN', max_length=16, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    price = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    currency = models.ForeignKey(Currency ,on_delete=models.PROTECT)
    summary = models.TextField(max_length= 2048, blank=True, null=True, help_text="Enter a brief description of the book")
    
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    
    
    def display_publishing_house(self):
        return ', '.join([ publishing_house.name for publishing_house in self.publishing_house.all()[:3] ])
    display_publishing_house.short_description = 'Publishing House'
    
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title

    class Meta():
        ordering = ['title']
