# Generated by Django 5.1 on 2024-08-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('customoer', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
