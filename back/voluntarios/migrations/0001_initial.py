# Generated by Django 5.1.1 on 2024-10-01 09:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Voluntarios',
            fields=[
                ('id_restaurante', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('CPF', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('grupo', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=128)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='voluntarios.endereco')),
            ],
        ),
    ]