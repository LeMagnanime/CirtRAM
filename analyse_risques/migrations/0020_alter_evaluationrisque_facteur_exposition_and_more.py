# Generated by Django 5.0.3 on 2024-06-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0019_domaine_evaluationrisque_facteur_exposition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationrisque',
            name='facteur_exposition',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='evaluationrisque',
            name='probabilite_occurrence',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
