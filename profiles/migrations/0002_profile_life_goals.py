# Generated by Django 3.2.13 on 2022-07-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='life_goals',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
