# Generated by Django 4.1.3 on 2022-11-17 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_patientr_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('room_discription', models.TextField(max_length=100)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
