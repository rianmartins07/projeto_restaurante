# Generated by Django 4.1.7 on 2023-05-25 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_user_nome_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]