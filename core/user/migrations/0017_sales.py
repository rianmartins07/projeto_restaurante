# Generated by Django 4.1.7 on 2023-06-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_remove_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id_order', models.IntegerField(primary_key=True, serialize=False)),
                ('table_id', models.IntegerField()),
                ('responsible_name', models.CharField(max_length=128)),
                ('table_number', models.IntegerField()),
                ('dish_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tessste',
                'managed': False,
            },
        ),
    ]
