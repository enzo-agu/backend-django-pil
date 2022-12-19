# Generated by Django 4.1.2 on 2022-10-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('age', models.IntegerField()),
                ('universe', models.CharField(choices=[('1', 'Marvel'), ('2', 'DC')], max_length=1, verbose_name='Universo')),
            ],
        ),
    ]
