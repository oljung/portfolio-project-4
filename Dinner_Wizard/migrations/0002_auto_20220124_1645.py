# Generated by Django 3.2 on 2022-01-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dinner_Wizard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='plan',
            name='dinners',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(related_name='recipe_categories', to='Dinner_Wizard.Category'),
        ),
    ]
