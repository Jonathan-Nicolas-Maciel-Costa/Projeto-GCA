# Generated by Django 3.2.12 on 2023-01-10 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_customuser_data_de_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_de_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone'),
        ),
    ]
