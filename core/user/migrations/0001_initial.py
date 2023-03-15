# Generated by Django 4.1.7 on 2023-03-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_index=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=81, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='endereco de email')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Prefiro não dizer', 'Prefiro Nao Dizer')], max_length=20)),
                ('data_nascimento', models.DateField(verbose_name='data de nascimento')),
                ('numero_celular', models.IntegerField()),
            ],
        ),
    ]