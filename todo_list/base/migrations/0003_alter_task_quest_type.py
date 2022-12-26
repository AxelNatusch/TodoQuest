# Generated by Django 4.0.4 on 2022-12-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_quest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='quest_type',
            field=models.CharField(choices=[('daily', 'Daily'), ('site', 'Site'), ('main', 'Main'), ('story', 'Story')], default='daily', max_length=20, null=True),
        ),
    ]
