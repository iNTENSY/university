# Generated by Django 5.0.4 on 2024-04-15 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.cards', to_field='identify_number', verbose_name='Ключ-карта'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='identify_number',
            field=models.CharField(max_length=150, unique=True, verbose_name='Уникальный номер'),
        ),
    ]