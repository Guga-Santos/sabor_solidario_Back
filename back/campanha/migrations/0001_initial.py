# Generated by Django 5.1.1 on 2024-10-01 10:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurantes', '0002_rename_cnjp_restaurantes_cnpj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id_campanha', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('quantidade', models.IntegerField()),
                ('tipo', models.CharField(max_length=64)),
                ('disponivel', models.BooleanField(default=True)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campanhas', to='restaurantes.restaurantes')),
            ],
        ),
    ]