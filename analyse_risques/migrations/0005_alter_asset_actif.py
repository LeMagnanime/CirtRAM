# Generated by Django 5.0.4 on 2024-05-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0004_typeactif_alter_asset_options_alter_asset_actif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='actif',
            field=models.CharField(max_length=200),
        ),
    ]
