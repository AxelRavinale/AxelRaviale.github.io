# Generated by Django 5.2.3 on 2025-07-10 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterModelOptions(
            name='localidad',
            options={'ordering': ['nombre']},
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='core.pais')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localidades', to='core.provincia'),
        ),
        migrations.AddConstraint(
            model_name='localidad',
            constraint=models.UniqueConstraint(fields=('provincia', 'nombre'), name='unique_localidad_por_provincia'),
        ),
        migrations.AddConstraint(
            model_name='provincia',
            constraint=models.UniqueConstraint(fields=('pais', 'nombre'), name='unique_provincia_por_pais'),
        ),
    ]
