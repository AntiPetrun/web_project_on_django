# Generated by Django 4.0.6 on 2022-07-17 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0014_bookseries_country_bookseries_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookseries',
            name='publish_house',
        ),
    ]
