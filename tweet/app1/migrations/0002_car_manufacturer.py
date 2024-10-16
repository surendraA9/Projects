# Generated by Django 5.1 on 2024-08-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('year', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('fuel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('ceo', models.CharField(max_length=50)),
                ('turnover', models.IntegerField()),
            ],
        ),
    ]
