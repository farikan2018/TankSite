# Generated by Django 3.2.3 on 2021-06-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_alter_tank_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='publish',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
