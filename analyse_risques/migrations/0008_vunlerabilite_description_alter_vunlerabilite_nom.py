# Generated by Django 5.0.4 on 2024-05-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0007_vunlerabilite'),
    ]

    operations = [
        migrations.AddField(
            model_name='vunlerabilite',
            name='description',
            field=models.TextField(default='pas de description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vunlerabilite',
            name='nom',
            field=models.CharField(max_length=200),
        ),
    ]
