# Generated by Django 4.0.4 on 2022-04-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(choices=[('Intro to Computer Science', 'Intro to Computer Science'), ('App Creation', 'App Creation'), ('Python Programming', 'Python Programming')], max_length=60),
        ),
    ]
