# Generated by Django 4.1.7 on 2023-05-14 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_managers_alter_user_data_nascimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
