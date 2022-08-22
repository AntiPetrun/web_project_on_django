# Generated by Django 4.0.6 on 2022-08-21 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_alter_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('in work', 'in work'), ('canceled', 'canceled'), ('delivered', 'delivered')], default='in work', help_text='Status of the Order', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular order across all orders', primary_key=True, serialize=False),
        ),
    ]