# Generated by Django 4.1.7 on 2023-04-12 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custommenu',
            name='status',
            field=models.IntegerField(verbose_name='ativo ou inativo'),
        ),
    ]
