# Generated by Django 5.1 on 2024-10-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0024_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='TService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srvc_t', models.CharField(max_length=500)),
            ],
        ),
    ]