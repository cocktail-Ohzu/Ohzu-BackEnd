# Generated by Django 3.0.8 on 2022-04-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_cocktail_base_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
