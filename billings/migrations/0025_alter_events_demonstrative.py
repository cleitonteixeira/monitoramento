# Generated by Django 5.0 on 2024-12-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0024_remove_events_typemoviment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='demonstrative',
            field=models.BooleanField(),
        ),
    ]
