# Generated by Django 4.1.3 on 2022-11-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_rename_lasname_worker_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='lastname',
            field=models.CharField(max_length=150, null=True, verbose_name='Introduza sus Apellidos'),
        ),
    ]
