# Generated by Django 5.0.4 on 2024-05-09 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse_risques', '0006_alter_asset_actif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vunlerabilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('type_actif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse_risques.typeactif')),
            ],
        ),
    ]
