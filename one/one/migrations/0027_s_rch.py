# Generated by Django 5.1 on 2024-09-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0026_f_rch'),
    ]

    operations = [
        migrations.CreateModel(
            name='S_rch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_rch_title', models.CharField(max_length=100)),
                ('s_rch_description', models.CharField(max_length=100)),
            ],
        ),
    ]