# Generated by Django 5.0.6 on 2024-07-10 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_contact_publishedmanager_alter_news_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublishedManager',
        ),
    ]
