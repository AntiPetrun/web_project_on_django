# Generated by Django 4.0.6 on 2022-07-17 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0009_alter_bookseries_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookseries',
            name='genre',
        ),
    ]
