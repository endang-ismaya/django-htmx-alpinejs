# Generated by Django 5.1.7 on 2025-03-21 06:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_article_word_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
