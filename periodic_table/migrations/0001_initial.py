# Generated by Django 5.1.4 on 2024-12-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=3, unique=True)),
                ('atomic_number', models.PositiveIntegerField(unique=True)),
                ('atomic_weight', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('group', models.PositiveIntegerField()),
                ('period', models.PositiveIntegerField()),
            ],
        ),
    ]
