# Generated by Django 3.0.8 on 2022-04-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220408_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail_base',
            name='amount',
        ),
    ]
