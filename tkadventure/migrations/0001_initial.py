# Generated by Django 3.1.1 on 2020-09-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('tour_type', models.CharField(choices=[('t', 'Trekking'), ('s', 'Safari'), ('i', 'Island'), ('m', 'More')], max_length=20)),
            ],
        ),
    ]
