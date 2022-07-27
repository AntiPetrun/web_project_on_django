from django.db import models


class Country(models.Model):
    name = models.CharField(max_length= 64, db_index=True)
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Countries'
        ordering = ['name']


class Language(models.Model):
    name = models.CharField(max_length= 32, db_index=True)
    
    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['name']


class Currency(models.Model):
    name = models.CharField(max_length= 16)
    code = models.CharField(max_length= 16, db_index=True)
    symbol = models.CharField(max_length= 16)
    
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
    address = models.TextField(max_length= 256, blank= True, null= True)
    web_site = models.URLField(blank= True, null= True)
    
    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['name']


class BookSeria(models.Model):
    title = models.CharField(max_length= 64, db_index=True)
    image = models.ImageField(blank= True, null= True)
    author = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, null=True, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, null=True, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.PROTECT)
    publishing_house = models.ForeignKey(PublishingHouse, null=True, on_delete=models.PROTECT)
    release_date = models.DateField(blank= True, null= True)
    description = models.TextField(max_length= 2048, blank= True, null= True)
    
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
    isbn = models.CharField(verbose_name='ISBN', max_length=16)
    price = models.FloatField(max_length=8)
    currency = models.ForeignKey(Currency ,on_delete=models.PROTECT)
    summary = models.TextField(max_length= 2048, blank=True, null=True)
    
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    
    def __str__(self):
        return self.title

    class Meta():
        ordering = ['title']
