# Generated by Django 4.1.7 on 2023-04-12 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_alter_menu_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='menu',
        ),
    ]