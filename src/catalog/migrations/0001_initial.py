# Generated by Django 4.0.6 on 2022-07-29 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_books', '0005_remove_bookseria_author_remove_bookseria_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('release_date', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=2048, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.author')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.country')),
                ('genre', models.ManyToManyField(help_text='Select a genre for this book seria', to='reference_books.genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.language')),
                ('publishing_house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.publishinghouse')),
            ],
            options={
                'verbose_name_plural': 'Book Series',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('release_number', models.CharField(max_length=16)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('page', models.IntegerField()),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=16, verbose_name='ISBN')),
                ('price', models.FloatField(max_length=8)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=2048, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.author')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.currency')),
                ('genre', models.ManyToManyField(help_text='Select a genre for this book', to='reference_books.genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.language')),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.publishinghouse')),
                ('seria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.bookseria')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]