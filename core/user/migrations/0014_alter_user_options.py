# Generated by Django 4.1.7 on 2023-05-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_user_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('generate_report', 'can generate and view report'),), 'verbose_name': 'user user', 'verbose_name_plural': 'users'},
        ),
    ]
