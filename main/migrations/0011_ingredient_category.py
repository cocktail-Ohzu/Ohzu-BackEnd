# Generated by Django 3.0.8 on 2022-07-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220625_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]