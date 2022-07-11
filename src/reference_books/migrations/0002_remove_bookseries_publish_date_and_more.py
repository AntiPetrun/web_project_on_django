# Generated by Django 4.0.6 on 2022-07-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookseries',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='bookseries',
            name='rus_publish_date',
        ),
        migrations.AddField(
            model_name='bookseries',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Release Date'),
        ),
        migrations.AddField(
            model_name='bookseries',
            name='rus_release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Release Date in Russian'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='founding_date',
            field=models.DateField(blank=True, null=True, verbose_name='Founding Date'),
        ),
    ]