# Generated by Django 4.1.3 on 2022-11-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_patient_p_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='p_adress',
            field=models.CharField(max_length=2000),
        ),
    ]
