# Generated by Django 4.1.7 on 2023-05-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nome',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Administrador', 1), ('Cozinha', 3), ('Garcom', 2)], max_length=30),
        ),
    ]
