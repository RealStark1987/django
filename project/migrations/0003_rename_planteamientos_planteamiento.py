# Generated by Django 4.1.3 on 2022-11-30 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_planteamientos_on_act'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Planteamientos',
            new_name='Planteamiento',
        ),
    ]