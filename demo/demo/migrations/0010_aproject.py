# Generated by Django 5.1 on 2024-10-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='AProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_description', models.CharField(max_length=500)),
            ],
        ),
    ]
