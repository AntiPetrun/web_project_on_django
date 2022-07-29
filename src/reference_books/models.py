from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length= 64, db_index=True)
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Countries'
        ordering = ['name']


class Language(models.Model):
    name = models.CharField(max_length= 32, db_index=True, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")
    
    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['name']


class Currency(models.Model):
    name = models.CharField(max_length= 32, help_text="Enter the currency like this: Euro, United States dollar, Japanese yen etc.")
    code = models.CharField(max_length= 16, db_index=True, help_text="Enter a graphic symbol used as a shorthand for a currency's name")
    symbol = models.CharField(max_length= 16, help_text='Enter ISO 4217 according to this list <a href="https://www.iso.org/iso-4217-currency-codes.html"></a>')
    
    def __str__(self):
        return self.code

    class Meta():
        verbose_name_plural = 'Currencies'
        ordering = ['code']


class Author(models.Model):
    first_name = models.CharField(max_length= 16)
    last_name = models.CharField(max_length= 32,db_index=True)
    country_of_birth = models.ForeignKey(Country, null=True, on_delete=models.PROTECT)
    date_of_birth = models.DateField(blank= True, null= True)
    date_of_death = models.DateField(blank= True, null= True)
    biography = models.TextField(max_length= 2048, blank= True, null= True)
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta():
        ordering = ['last_name']


class Genre(models.Model):
    name = models.CharField(max_length= 32, db_index=True, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    description = models.TextField(max_length= 2048, blank= True, null= True)
    
    def __str__(self):
        return self.name

    class Meta():
        ordering = ['name']


class PublishingHouse(models.Model):
    name = models.CharField(max_length= 32, db_index=True)
    founding_date = models.DateField(blank= True, null= True)
    country = models.ForeignKey(Country, null=True, on_delete=models.PROTECT)
    address = models.TextField(max_length= 256, blank= True, null= True, help_text="Enter full address including courty, state etc.")
    web_site = models.URLField(blank= True, null= True, help_text="Enter web-site like this: https://antipetrun86.pythonanywhere.com")
    
    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['name']
