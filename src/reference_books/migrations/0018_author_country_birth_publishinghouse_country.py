# Generated by Django 4.0.6 on 2022-07-17 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0017_remove_author_country_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='country_birth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.country', verbose_name='Country of Birth'),
        ),
        migrations.AddField(
            model_name='publishinghouse',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_books.country', verbose_name='Country'),
        ),
    ]
