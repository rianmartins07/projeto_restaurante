# Generated by Django 4.1.7 on 2023-05-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('PEDIDO NA COZINHA', 'Pedido Na Cozinha'), ('PRONTO', 'Pronto'), ('EM PREPARO', 'Em Preparo'), ('CANCELADO', 'Cancelado')], default='EM PREPARO', max_length=30),
        ),
    ]