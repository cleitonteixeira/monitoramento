# Generated by Django 5.0 on 2024-12-12 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0035_itensrequisicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisicao',
            name='type',
        ),
    ]
