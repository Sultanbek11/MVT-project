# Generated by Django 4.1.1 on 2022-09-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_match', models.DateField()),
                ('opponent', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Trophies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_trophies', models.CharField(max_length=20)),
                ('years_of_win', models.DateField()),
            ],
        ),
    ]
