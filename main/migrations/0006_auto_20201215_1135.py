# Generated by Django 2.2.17 on 2020-12-15 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201215_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posted_at',
            new_name='created_at',
        ),
    ]
