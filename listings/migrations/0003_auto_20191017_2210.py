# Generated by Django 2.2.5 on 2019-10-17 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191017_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='Calories',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='Servings',
        ),
    ]
