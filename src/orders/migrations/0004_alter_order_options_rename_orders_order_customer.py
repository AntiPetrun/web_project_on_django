# Generated by Django 4.0.6 on 2022-08-21 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_comments_remove_order_delivery_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_date'], 'permissions': (('can_edit_order', 'Edit order(s)'),)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orders',
            new_name='customer',
        ),
    ]
