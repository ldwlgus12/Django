# Generated by Django 3.2.18 on 2023-04-17 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(to='hospitals.Doctor'),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
