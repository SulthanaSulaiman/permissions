# Generated by Django 3.0.4 on 2020-06-13 18:36

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0037_auto_20200607_1628'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='element',
            managers=[
                ('activated', django.db.models.manager.Manager()),
            ],
        ),
    ]
