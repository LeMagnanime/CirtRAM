# Generated by Django 5.0.4 on 2024-05-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0013_rename_misque_analyse_risque_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_menace', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('vulnerabilte', models.ManyToManyField(to='analyse_risques.vunlerabilite')),
            ],
        ),
    ]
