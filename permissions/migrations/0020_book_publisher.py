# Generated by Django 3.0.4 on 2020-05-16 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_auto_20200516_1312'),
        ('permissions', '0019_element_denied_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publisher.Publisher'),
        ),
    ]
