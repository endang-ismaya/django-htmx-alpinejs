# Generated by Django 5.1.7 on 2025-03-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='word_count',
            field=models.IntegerField(default=0),
        ),
    ]
