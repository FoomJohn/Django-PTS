# Generated by Django 5.0.1 on 2024-03-30 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_status_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pn_all_total', models.IntegerField(default=0)),
                ('sw_all_total', models.IntegerField(default=0)),
                ('eg_all_total', models.IntegerField(default=0)),
                ('fq_all_total', models.IntegerField(default=0)),
                ('t_all_avg', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.candidate')),
            ],
        ),
    ]
