# Generated by Django 2.2.2 on 2020-01-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_candidate_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]