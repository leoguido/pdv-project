# Generated by Django 3.2.8 on 2021-10-21 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_models', '0007_cortecaja_caja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cortecaja',
            name='caja',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corte', to='manage_models.caja'),
        ),
    ]
