# Generated by Django 4.0.6 on 2022-07-20 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0020_alter_literarygenre_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=16, verbose_name='Name')),
                ('code', models.CharField(db_index=True, max_length=16, verbose_name='Name')),
                ('symbol', models.CharField(db_index=True, max_length=16, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Literary Genre',
                'verbose_name_plural': 'Literary Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='Name')),
                ('original_name', models.CharField(max_length=32, verbose_name='Original Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('release_number', models.CharField(max_length=16, verbose_name='Realise Number')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('rus_release_date', models.DateField(blank=True, null=True, verbose_name='Release Date in Russian')),
                ('page', models.CharField(max_length=16, verbose_name='Pages')),
                ('isbn', models.IntegerField(max_length=16, verbose_name='ISBN')),
                ('price', models.FloatField(max_length=8, verbose_name='Price')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.author', verbose_name='Author')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.country', verbose_name='Country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.currency', verbose_name='Currency')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.literarygenre', verbose_name='Genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.language', verbose_name='Language')),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.publishinghouse', verbose_name='Publishing House')),
                ('seria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_books.bookseries', verbose_name='Series')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['name'],
            },
        ),
    ]
