# Generated by Django 4.1.3 on 2023-01-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aluno', '0003_alter_aproveitamento_de_disciplina_comprovante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aproveitamento_de_disciplina',
            name='comprovante',
            field=models.FileField(max_length=1000, upload_to='documentos', verbose_name='Comprovante'),
        ),
        migrations.AlterField(
            model_name='aproveitamento_de_disciplina',
            name='historico',
            field=models.FileField(max_length=1000, upload_to='documentos', verbose_name='Historico'),
        ),
    ]