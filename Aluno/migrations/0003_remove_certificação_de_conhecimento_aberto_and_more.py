# Generated by Django 4.1.6 on 2023-02-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluno', '0002_certificação_de_conhecimento_aberto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificação_de_conhecimento',
            name='aberto',
        ),
        migrations.RemoveField(
            model_name='certificação_de_conhecimento',
            name='data_final',
        ),
    ]
