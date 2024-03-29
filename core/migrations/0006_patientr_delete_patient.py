# Generated by Django 4.1.3 on 2022-11-12 14:27

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_patient_p_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientR',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('marital', models.CharField(max_length=20)),
                ('lga', models.CharField(max_length=100)),
                ('p_adress', models.TextField(blank=True)),
                ('state', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=1000)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
