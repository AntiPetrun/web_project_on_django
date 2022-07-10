from email.mime import image
from pyexpat import model
from django.db import models
from django.forms import DateField


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        verbose_name= 'First Name',
        max_length= 16
        )
    last_name = models.CharField(
        verbose_name= 'Last Name',
        max_length= 32
    )
    short_name = models.CharField(
        verbose_name= 'Short Name',
        max_length= 32
    )
    country_birth = models.CharField(
        verbose_name= 'Country of Birth',
        max_length= 32
    )
    date_birth = models.DateField(
        verbose_name= 'Date of Birth',
        blank= True,
        null= True
    )
    biography = models.TextField(
        verbose_name= 'Biography',
        max_length= 256
    )
    
    
    def __str__(self) -> str:
        return self.short_name


class BookSeries(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 32
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
    author = models.CharField(
        verbose_name= 'Author',
        max_length= 32
    )
    genre = models.CharField(
        verbose_name= 'Genre',
        max_length= 32
    )
    country = models.CharField(
        verbose_name= 'Country',
        max_length= 32
    )
    language = models.CharField(
        verbose_name= 'Language',
        max_length= 32
    )
    publish_house = models.CharField(
        verbose_name= 'Publishing House',
        max_length= 32
    )
    publish_date = models.ImageField(
        verbose_name= 'Publication Date',
        blank= True,
        null= True
    )
    rus_publish_date = models.ImageField(
        verbose_name= 'Publication Date on Russian',
        blank= True,
        null= True
    )
    
    
    def __str__(self) -> str:
        return self.name


class LiteraryGenre(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 32
    )
    description = models.TextField(
        verbose_name= 'Biography',
        max_length= 256
    )
    
    
    def __str__(self) -> str:
        return self.name


class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name= 'Name',
        max_length= 32
    )
    country = models.CharField(
        verbose_name= 'Country',
        max_length= 32
    )
    founding_date = models.ImageField(
        verbose_name= 'Founding Date',
        blank= True,
        null= True
    )
    address = models.TextField(
        verbose_name= 'Address',
        max_length= 256
    )
    web_site = models.URLField(
        verbose_name= 'Web Site',
        blank= True,
        null= True
    )
    
    
    def __str__(self) -> str:
        return self.name
