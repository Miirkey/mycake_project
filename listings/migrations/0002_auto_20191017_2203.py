# Generated by Django 2.2.5 on 2019-10-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Calories',
            field=models.IntegerField(default=985),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='Servings',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='Ingredients',
            field=models.TextField(max_length=200),
        ),
    ]
