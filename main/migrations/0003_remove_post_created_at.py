# Generated by Django 2.2.17 on 2020-12-15 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]
