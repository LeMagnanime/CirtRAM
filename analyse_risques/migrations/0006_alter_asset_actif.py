# Generated by Django 5.0.4 on 2024-05-09 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0005_alter_asset_actif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='actif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse_risques.typeactif'),
        ),
    ]
