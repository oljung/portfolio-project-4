# Generated by Django 3.2 on 2022-01-25 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredient_list', models.ManyToManyField(related_name='shopping_ingredients', to='Dinner_Wizard.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=100)),
                ('description', models.TextField(default='Write your description here')),
                ('categories', models.ManyToManyField(related_name='recipe_categories', to='Dinner_Wizard.Category')),
                ('favourites', models.ManyToManyField(blank=True, related_name='recipe_favourites', to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.ManyToManyField(related_name='recipe_ingredients', to='Dinner_Wizard.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Upcoming'), (1, 'Active'), (2, 'Previous')], default=0)),
                ('recipes', models.ManyToManyField(related_name='dinner_recipes', to='Dinner_Wizard.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinner_plan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
