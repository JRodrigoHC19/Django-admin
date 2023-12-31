# Generated by Django 4.2.5 on 2023-09-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_categoria_pub_date_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('dni', models.IntegerField(default=0)),
                ('telefono', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=150)),
                ('correo', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('fecha_pub', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
