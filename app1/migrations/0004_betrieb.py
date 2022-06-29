# Generated by Django 4.0.5 on 2022-06-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_az_zustaendigkeit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betrieb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma', models.CharField(max_length=255)),
                ('bemerkung', models.CharField(blank=True, max_length=255)),
                ('telefon_zentrale', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
