# Generated by Django 3.2.7 on 2021-09-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0013_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AlterField(
            model_name='comment',
            name='ticket_comment',
            field=models.CharField(max_length=50),
        ),
    ]
