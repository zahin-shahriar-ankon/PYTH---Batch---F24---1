# Generated by Django 5.1 on 2024-09-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0042_delete_sc_dr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sc_dr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_duration', models.CharField(max_length=100)),
            ],
        ),
    ]