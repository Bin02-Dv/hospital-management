# Generated by Django 4.1.3 on 2022-11-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_p_adress_patientr_addrss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientr',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]