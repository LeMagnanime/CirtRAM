# Generated by Django 5.0.4 on 2024-05-09 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0008_vunlerabilite_description_alter_vunlerabilite_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyse',
            name='Vulnérabilité',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse_risques.vunlerabilite'),
        ),
    ]
