# Generated by Django 3.1.1 on 2020-09-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkadventure', '0007_tour_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_type',
            field=models.CharField(choices=[('Trekking', 'Trekking'), ('Safari', 'Safari'), ('Island', 'Island'), ('More', 'More')], max_length=20),
        ),
    ]
