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
    country_birth = models.CharField(
        verbose_name= 'Country of Birth',
        max_length= 32,
        blank= True,
        null= True
    )
    date_birth = models.DateField(
        verbose_name= 'Date of Birth',
        blank= True,
        null= True
    )
    biography = models.TextField(
        verbose_name= 'Biography',
        max_length= 256,
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
        max_length= 32,
        db_index=True
    )
    original_name = models.CharField(
        verbose_name= 'Original Name',
        max_length= 32
    )
    image = models.ImageField(
        verbose_name= 'Image',
        blank= True,
        null= True
    )
    genre = models.CharField(
        verbose_name= 'Genre',
        max_length= 32
    )
    country = models.CharField(
        verbose_name= 'Country',
        max_length= 32,
        blank= True,
        null= True
    )
    language = models.CharField(
        verbose_name= 'Language',
        max_length= 32,
        blank= True,
        null= True
    )
    publish_house = models.CharField(
        verbose_name= 'Publishing House',
        max_length= 32,
        blank= True,
        null= True
    )
    release_date = models.DateField(
        verbose_name= 'Release Date',
        blank= True,
        null= True
    )
    rus_release_date = models.DateField(
        verbose_name= 'Release Date in Russian',
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
        verbose_name= 'Biography',
        max_length= 256,
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
    country = models.CharField(
        verbose_name= 'Country',
        max_length= 32,
        blank= True,
        null= True
    )
    founding_date = models.DateField(
        verbose_name= 'Founding Date',
        blank= True,
        null= True
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
