# Generated by Django 5.0.6 on 2024-08-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
