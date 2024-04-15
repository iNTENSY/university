# Generated by Django 5.0.4 on 2024-04-15 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='card',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='attendance.cards', verbose_name='Пользователь'),
        ),
    ]