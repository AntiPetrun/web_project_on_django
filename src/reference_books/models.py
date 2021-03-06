from email.mime import image
from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import DateField


class Author(models.Model):
    first_name = models.CharField(
        verbose_name= 'First Name',
        max_length= 16
        )
    last_name = models.CharField(
        verbose_name= 'Last Name',
        max_length= 32,
        db_index=True
    )
    full_name = models.CharField(
        verbose_name= 'Full Name',
        max_length= 32
    )
    country_birth = models.ForeignKey(
        'Country',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Country of Birth'
    )
    date_birth = models.DateField(
        verbose_name= 'Date of Birth',
        blank= True,
        null= True
    )
    biography = models.TextField(
        verbose_name= 'Biography',
        max_length= 2048,
        blank= True,
        null= True
    )
    
    def __str__(self) -> str:
        return self.full_name


    class Meta():
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'
        ordering = ['last_name']


class BookSeries(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 64,
        db_index=True
    )
    original_name = models.CharField(
        verbose_name= 'Original Name',
        max_length= 64
    )
    image = models.ImageField(
        verbose_name= 'Image',
        blank= True,
        null= True
    )
    author = models.ForeignKey(
        'Author',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Author'
    )
    country = models.ForeignKey(
        'Country',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Country'
    )
    language = models.ForeignKey(
        'Language',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Language'
    )
    genre = models.ForeignKey(
        'LiteraryGenre',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Genre'
    )
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Publishing House'
    )
    release_date = models.DateField(
        verbose_name= 'Release Date',
        blank= True,
        null= True
    )
    description = models.TextField(
        verbose_name= 'Description',
        max_length= 2048,
        blank= True,
        null= True
    )
    
    def __str__(self) -> str:
        return self.name

    
    class Meta():
        verbose_name_plural = 'Book Series'
        verbose_name = 'Book Series'
        ordering = ['name']


class LiteraryGenre(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 32,
        db_index=True
    )
    description = models.TextField(
        verbose_name= 'Description',
        max_length= 2048,
        blank= True,
        null= True
    )
    
    def __str__(self) -> str:
        return self.name


    class Meta():
        verbose_name_plural = 'Literary Genres'
        verbose_name = 'Literary Genre'
        ordering = ['name']


class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 32,
        db_index=True
    )
    founding_date = models.DateField(
        verbose_name= 'Founding Date',
        blank= True,
        null= True
    )
    country = models.ForeignKey(
        'Country',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Country'
    )
    address = models.TextField(
        verbose_name= 'Address',
        max_length= 256,
        blank= True,
        null= True
    )
    web_site = models.URLField(
        verbose_name= 'Web Site',
        blank= True,
        null= True
    )
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta():
        verbose_name_plural = 'Publishing Houses'
        verbose_name = 'Publishing House'
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 64,
        db_index=True
    )
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta():
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'
        ordering = ['name']


class Language(models.Model):
    name = models.CharField(
        verbose_name= 'Language',
        max_length= 32,
        db_index=True
    )
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta():
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'
        ordering = ['name']


class Currency(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 16,
        db_index=True
    )
    code = models.CharField(
        verbose_name= 'Code',
        max_length= 16,
        db_index=True
    )
    symbol = models.CharField(
        verbose_name= 'Symbol',
        max_length= 16,
        db_index=True
    )
    
    def __str__(self) -> str:
        return self.code


    class Meta():
        verbose_name_plural = 'Currencies'
        verbose_name = 'Currency'
        ordering = ['code']


class Book(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 64,
        db_index=True
    )
    original_name = models.CharField(
        verbose_name= 'Original Name',
        max_length= 64
    )
    image = models.ImageField(
        verbose_name= 'Image',
        blank= True,
        null= True
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.PROTECT,
        verbose_name='Author'
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.PROTECT,
        verbose_name='Country'
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.PROTECT,
        verbose_name='Language'
    )
    seria = models.ForeignKey(
        'BookSeries',
        on_delete=models.PROTECT,
        verbose_name='Series'
    )
    release_number = models.CharField(
        verbose_name= 'Realise Number',
        max_length= 16
    )
    genre = models.ForeignKey(
        'LiteraryGenre',
        on_delete=models.PROTECT,
        verbose_name='Genre'
    )
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.PROTECT,
        verbose_name='Publishing House'
    )
    release_date = models.DateField(
        verbose_name= 'Release Date',
        blank= True,
        null= True
    )
    page = models.IntegerField(
        verbose_name= 'Pages',
    )
    isbn = models.CharField(
        verbose_name= 'ISBN',
        max_length= 16
    )
    price = models.FloatField(
        verbose_name='Price',
        max_length=8
    )
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.PROTECT,
        verbose_name='Currency'
    )
    description = models.TextField(
        verbose_name= 'Description',
        max_length= 2048,
        blank= True,
        null= True
    )
    
    def __str__(self) -> str:
        return self.name

    
    class Meta():
        verbose_name_plural = 'Books'
        verbose_name = 'Book'
        ordering = ['name']
