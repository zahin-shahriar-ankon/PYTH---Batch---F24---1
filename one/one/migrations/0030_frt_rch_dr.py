# Generated by Django 5.1 on 2024-09-29 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0029_frt_rch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frt_rch_dr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frt_rch_dr', models.CharField(max_length=100)),
            ],
        ),
    ]
