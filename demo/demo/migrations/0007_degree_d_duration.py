# Generated by Django 5.1 on 2024-10-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='d_duration',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]