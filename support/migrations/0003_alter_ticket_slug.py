# Generated by Django 3.2.7 on 2021-09-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_alter_ticket_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(),
        ),
    ]