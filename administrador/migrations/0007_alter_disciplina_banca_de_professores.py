# Generated by Django 4.1.6 on 2023-02-04 23:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrador', '0006_alter_disciplina_banca_de_professores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='banca_de_professores',
            field=models.ManyToManyField(related_name='professores', to=settings.AUTH_USER_MODEL, verbose_name='Professores'),
        ),
    ]
