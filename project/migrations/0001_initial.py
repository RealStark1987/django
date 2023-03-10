# Generated by Django 4.1.3 on 2022-11-30 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Introduza el Nombre')),
                ('lasname', models.CharField(max_length=150, verbose_name='Introduza sus Apellidos')),
                ('user_uci', models.CharField(max_length=50, null=True, verbose_name='Introduzca su usuario UCI')),
                ('correo', models.CharField(max_length=254, null=True, verbose_name='Introduza su Correo ')),
                ('age', models.PositiveSmallIntegerField(null=True, verbose_name='Introduza su Edad ')),
                ('sexo', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=1, verbose_name='Introduza su Sexo ')),
                ('DNI', models.CharField(blank=True, max_length=11, null=True, verbose_name='Introduza su Carnet de Identidad')),
                ('address', models.TextField(default='', max_length=200, null=True, verbose_name='Diga su Direccion')),
                ('cell', models.CharField(max_length=11, null=True, verbose_name='Introduza su Telefono')),
                ('occupation', models.TextField(choices=[('Profesor', 'Profesor'), ('Tecnico', 'Tecnico'), ('Auxiliar', 'Auxiliar'), ('Secretario', 'Secretario'), ('Jefe de Area', 'Jefe de Area')], null=True, verbose_name='Ocupacion')),
                ('salary', models.FloatField(null=True, verbose_name='Introduza el Salario ')),
                ('civil_state', models.TextField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viudo')], verbose_name='Estado Civil')),
                ('kids', models.PositiveSmallIntegerField(verbose_name='Hijos')),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Agregado Por: ')),
            ],
        ),
        migrations.CreateModel(
            name='Planteamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=80, null=True, verbose_name='Nombre del Planteamiento')),
                ('name', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateField()),
                ('description', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('created', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creada Por:')),
            ],
        ),
    ]
