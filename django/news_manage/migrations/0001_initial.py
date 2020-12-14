# Generated by Django 3.1.2 on 2020-10-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('news_url', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]