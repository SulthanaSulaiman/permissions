# Generated by Django 3.0.4 on 2020-05-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0016_auto_20200503_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='followedup_at',
            field=models.DateField(null=True),
        ),
    ]