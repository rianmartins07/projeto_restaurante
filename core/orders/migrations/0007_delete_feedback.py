# Generated by Django 4.1.7 on 2023-05-17 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_feedback_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
