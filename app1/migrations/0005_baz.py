# Generated by Django 4.0.5 on 2022-06-28 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_betrieb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ausbildungszweig', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.az_zustaendigkeit')),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.betrieb')),
            ],
        ),
    ]