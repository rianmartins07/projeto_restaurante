# Generated by Django 4.1.7 on 2023-03-15 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='numero_celular',
            field=models.CharField(max_length=15, verbose_name='numero de celular'),
        ),
    ]
