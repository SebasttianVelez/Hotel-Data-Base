# Generated by Django 2.0.7 on 2018-07-05 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Habitacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_habitacion',
            fields=[
                ('idTipo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='habitacion',
            name='fkTipo',
            field=models.ForeignKey(null=True, on_delete=None, to='Habitacion.tipo_habitacion'),
        ),
    ]
