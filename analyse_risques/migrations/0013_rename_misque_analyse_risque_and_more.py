# Generated by Django 5.0.4 on 2024-05-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0012_rename_actif_asset_type_actif_asset_nom_actif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analyse',
            old_name='misque',
            new_name='risque',
        ),
        migrations.AlterField(
            model_name='analyse',
            name='probabilite_occurrence',
            field=models.FloatField(),
        ),
    ]
