# Generated by Django 4.0.6 on 2022-07-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0004_alter_author_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
            ],
        ),
    ]
