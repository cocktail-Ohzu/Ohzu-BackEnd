# Generated by Django 3.0.8 on 2022-06-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220622_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='img2',
            field=models.URLField(null=True),
        ),
    ]