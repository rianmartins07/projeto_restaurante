# Generated by Django 4.1.7 on 2023-05-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='motivo de cancelamento',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
