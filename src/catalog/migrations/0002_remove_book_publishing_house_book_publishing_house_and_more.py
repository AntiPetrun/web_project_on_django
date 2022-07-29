# Generated by Django 4.0.6 on 2022-07-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0005_remove_bookseria_author_remove_bookseria_country_and_more'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publishing_house',
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ManyToManyField(help_text='Select a Publishing House for this book', to='reference_books.publishinghouse'),
        ),
        migrations.RemoveField(
            model_name='bookseria',
            name='publishing_house',
        ),
        migrations.AddField(
            model_name='bookseria',
            name='publishing_house',
            field=models.ManyToManyField(help_text='Select a Publishing House for this book', to='reference_books.publishinghouse'),
        ),
    ]
