# Generated by Django 3.2.8 on 2021-10-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_models', '0013_alter_cortecaja_saldo_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cortecaja',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
    ]