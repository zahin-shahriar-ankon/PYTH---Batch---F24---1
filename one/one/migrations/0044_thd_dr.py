# Generated by Django 5.1 on 2024-09-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0043_sc_dr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thd_dr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thd_duration', models.CharField(max_length=100)),
            ],
        ),
    ]
