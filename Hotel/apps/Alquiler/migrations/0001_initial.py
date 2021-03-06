# Generated by Django 2.0.7 on 2018-07-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Registrador', '0001_initial'),
        ('Habitacion', '0005_auto_20180705_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('idAlquiler', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fechaHoraEntrada', models.DateTimeField(auto_now_add=True)),
                ('fechaHoraSalida', models.DateTimeField()),
                ('costoTotal', models.IntegerField(default=0)),
                ('observacion', models.TextField()),
                ('fkCliente', models.ForeignKey(on_delete=None, to='Cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='alquiler',
            name='fkEstado',
            field=models.ForeignKey(null=True, on_delete=None, to='Alquiler.Estado'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='fkHabitacion',
            field=models.ForeignKey(on_delete=None, to='Habitacion.Habitacion'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='fkRegistrador',
            field=models.ForeignKey(on_delete=None, to='Registrador.Registrador'),
        ),
    ]
