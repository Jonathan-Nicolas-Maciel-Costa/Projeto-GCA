# Generated by Django 4.1.6 on 2023-02-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_alter_disciplina_banca_de_professores'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='status',
            field=models.CharField(choices=[('Cursando', 'Cursando'), ('Aprovado', 'Aprovado'), ('Espera', 'Espera')], default='Cursando', max_length=20, verbose_name='Status'),
        ),
    ]
