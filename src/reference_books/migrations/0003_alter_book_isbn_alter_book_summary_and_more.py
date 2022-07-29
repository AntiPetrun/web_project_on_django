# Generated by Django 4.0.6 on 2022-07-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0002_remove_book_genre_book_genre_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=16, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=2048, null=True),
        ),
        migrations.RemoveField(
            model_name='bookseria',
            name='genre',
        ),
        migrations.AddField(
            model_name='bookseria',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book seria', to='reference_books.genre'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(db_index=True, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=32),
        ),
    ]