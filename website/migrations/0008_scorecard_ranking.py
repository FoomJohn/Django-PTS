# Generated by Django 5.0.1 on 2024-03-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_scorecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecard',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]