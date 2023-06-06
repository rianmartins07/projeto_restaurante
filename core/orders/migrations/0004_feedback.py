# Generated by Django 4.1.7 on 2023-05-17 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0002_alter_table_table'),
        ('orders', '0003_rename_dish_id_orders_dish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(choices=[('Muito ruim', 'Muito Ruim'), ('Ruim', 'Ruim'), ('Regular', 'Regular'), ('Bom', 'Bom'), ('Muito bom', 'Muito Bom')], max_length=30)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waiter.table')),
            ],
            options={
                'db_table': 'table_feedback',
                'managed': True,
            },
        ),
    ]