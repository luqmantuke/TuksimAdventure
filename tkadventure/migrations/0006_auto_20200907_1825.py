# Generated by Django 3.1.1 on 2020-09-07 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tkadventure', '0005_auto_20200907_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='user_name',
        ),
        migrations.AddField(
            model_name='bookings',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tkadventure.tour'),
        ),
    ]
