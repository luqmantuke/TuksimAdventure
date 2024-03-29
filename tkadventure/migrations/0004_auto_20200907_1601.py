# Generated by Django 3.1.1 on 2020-09-07 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tkadventure', '0003_auto_20200907_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_descr',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tkadventure.tour')),
            ],
        ),
    ]
