# Generated by Django 5.0 on 2024-11-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0008_cost_created_at_cost_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]