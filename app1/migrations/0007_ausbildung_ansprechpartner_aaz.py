# Generated by Django 4.0.5 on 2022-06-28 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_bewerbung_bewertung_standort_praktikum_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ausbildung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginn', models.DateField()),
                ('ende', models.DateField()),
                ('abschluss', models.BooleanField(blank=True)),
                ('ausbildungszweig', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.az_zustaendigkeit')),
                ('teilnehmer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.teilnehmer')),
            ],
        ),
        migrations.CreateModel(
            name='Ansprechpartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anrede', models.CharField(max_length=20)),
                ('titel', models.CharField(blank=True, max_length=20)),
                ('vname', models.CharField(blank=True, max_length=255)),
                ('nname', models.CharField(max_length=255)),
                ('telefon', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('bemerkung', models.TextField(blank=True)),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.betrieb')),
            ],
        ),
        migrations.CreateModel(
            name='Aaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ansprechpartner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.ansprechpartner')),
                ('zustaendigkeit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.az_zustaendigkeit')),
            ],
        ),
    ]
