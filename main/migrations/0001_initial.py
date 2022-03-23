# Generated by Django 3.0.8 on 2022-03-23 16:08

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'BaseTag',
                'verbose_name_plural': 'BaseTags',
            },
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('eng_name', models.CharField(max_length=20)),
                ('img', models.URLField()),
                ('desc', models.CharField(max_length=50)),
                ('strength', models.IntegerField()),
                ('color', models.CharField(max_length=10)),
                ('recipe', models.TextField()),
                ('ohzu_point', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FlavorTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'FlavorTag',
                'verbose_name_plural': 'FlavorTags',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientsRecTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'IngredientsRecTag',
                'verbose_name_plural': 'IngredientsRecTags',
            },
        ),
        migrations.CreateModel(
            name='MoodTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'MoodTag',
                'verbose_name_plural': 'MoodTags',
            },
        ),
        migrations.CreateModel(
            name='OrnamentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'OrnamentTag',
                'verbose_name_plural': 'OrnamentTags',
            },
        ),
        migrations.CreateModel(
            name='WeatherSeasonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'WeatherSeasonTag',
                'verbose_name_plural': 'WeatherSeasonTags',
            },
        ),
        migrations.CreateModel(
            name='ThroughWeatherSeasonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_throughweatherseasontag_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.WeatherSeasonTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThroughOrnamentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_throughornamenttag_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.OrnamentTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThroughMoodTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_throughmoodtag_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MoodTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThroughIngredientsRecTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_throughingredientsrectag_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.IngredientsRecTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThroughFlavorTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_throughflavortag_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FlavorTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThroughBaseTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_throughbasetag_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BaseTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cocktail_Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=20)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cocktail')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='base',
            field=taggit.managers.TaggableManager(help_text='List all the available base tags here.', through='main.ThroughBaseTag', to='main.BaseTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='flavor',
            field=taggit.managers.TaggableManager(help_text='List all the available flavor tags here.', through='main.ThroughFlavorTag', to='main.FlavorTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ingredients_rec',
            field=taggit.managers.TaggableManager(blank=True, help_text='List all the available ingredients_rec tags here.', through='main.ThroughIngredientsRecTag', to='main.IngredientsRecTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='mood',
            field=taggit.managers.TaggableManager(help_text='List all the available mood tags here.', through='main.ThroughMoodTag', to='main.MoodTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ornament',
            field=taggit.managers.TaggableManager(blank=True, help_text='List all the available ornament tags here.', through='main.ThroughOrnamentTag', to='main.OrnamentTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='weather_and_season',
            field=taggit.managers.TaggableManager(help_text='List all the available weather and season tags here.', through='main.ThroughWeatherSeasonTag', to='main.WeatherSeasonTag', verbose_name='Tags'),
        ),
    ]