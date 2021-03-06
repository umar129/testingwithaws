# Generated by Django 3.1.1 on 2021-03-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostumerRegistration',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('number', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('address', models.TextField(max_length=200)),
                ('pwd', models.CharField(max_length=10)),
                ('dor', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
