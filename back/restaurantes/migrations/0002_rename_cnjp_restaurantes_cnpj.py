# Generated by Django 5.1.1 on 2024-10-01 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantes',
            old_name='CNJP',
            new_name='CNPJ',
        ),
    ]
