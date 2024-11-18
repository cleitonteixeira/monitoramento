# Generated by Django 5.0 on 2024-11-08 12:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0006_alter_branch_created_at_alter_typebranch_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='supplier',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]