# Generated by Django 4.0.5 on 2022-06-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orte',
            fields=[
                ('plz', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ort', models.CharField(max_length=255)),
            ],
        ),
    ]