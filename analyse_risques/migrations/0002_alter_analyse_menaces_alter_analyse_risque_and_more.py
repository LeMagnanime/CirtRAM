# Generated by Django 5.0.4 on 2024-05-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyse',
            name='Menaces',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='Risque',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='Vulnérabilité',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='asset',
            name='actif',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
