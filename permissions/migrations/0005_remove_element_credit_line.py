# Generated by Django 3.0.4 on 2020-04-09 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0004_element_credit_line'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='credit_line',
        ),
    ]