# Generated by Django 2.2.17 on 2020-12-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]