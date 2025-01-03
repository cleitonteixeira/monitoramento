# Generated by Django 5.0 on 2024-12-13 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0037_alter_requisicao_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cod', models.CharField(max_length=12, unique=True)),
                ('unidade', models.CharField(max_length=4)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='itensrequisicao',
            name='item_id',
        ),
        migrations.AddField(
            model_name='itensrequisicao',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billings.produtos'),
        ),
    ]
