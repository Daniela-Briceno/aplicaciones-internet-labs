# Generated by Django 3.2.3 on 2023-10-22 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('alumnos', models.IntegerField()),
                ('codigo', models.CharField(max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_id', to='course_management.curso')),
            ],
        ),
    ]
