# Generated by Django 5.1 on 2024-09-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_collab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_title', models.CharField(max_length=100)),
                ('t_description', models.CharField(max_length=100)),
            ],
        ),
    ]
