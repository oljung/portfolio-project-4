# Generated by Django 3.2 on 2022-01-31 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dinner_Wizard', '0004_auto_20220131_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='ingredient_list',
            field=models.ManyToManyField(blank=True, related_name='shopping_ingredients', to='Dinner_Wizard.Ingredient'),
        ),
    ]