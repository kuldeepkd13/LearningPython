# Generated by Django 4.1.10 on 2023-08-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
