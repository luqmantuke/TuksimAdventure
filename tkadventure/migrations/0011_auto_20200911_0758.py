# Generated by Django 3.1.1 on 2020-09-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkadventure', '0010_auto_20200910_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tour',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]