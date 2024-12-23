# Generated by Django 5.0 on 2024-10-17 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('period', models.DateField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.IntegerField()),
                ('supplier', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('value', models.FloatField()),
                ('expiration', models.DateField()),
                ('branch_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billings.branch')),
            ],
        ),
    ]
