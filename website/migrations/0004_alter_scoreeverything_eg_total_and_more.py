# Generated by Django 5.0.1 on 2024-03-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_scoreeverything'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreeverything',
            name='eg_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreeverything',
            name='fq_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreeverything',
            name='pn_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreeverything',
            name='sw_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreeverything',
            name='t_avg',
            field=models.IntegerField(default=0),
        ),
    ]