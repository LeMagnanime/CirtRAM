# Generated by Django 5.0.4 on 2024-05-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0011_rename_criticité_analyse_criticite_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='actif',
            new_name='type_actif',
        ),
        migrations.AddField(
            model_name='asset',
            name='nom_actif',
            field=models.CharField(default='Actif primaire', max_length=200),
            preserve_default=False,
        ),
    ]
