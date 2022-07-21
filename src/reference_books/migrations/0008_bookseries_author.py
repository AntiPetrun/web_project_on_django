# Generated by Django 4.0.6 on 2022-07-17 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0007_alter_author_options_alter_bookseries_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookseries',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.author', verbose_name='Author'),
        ),
    ]