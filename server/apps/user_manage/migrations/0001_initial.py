# Generated by Django 3.0.7 on 2020-12-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=200)),
                ('fund_code', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=20)),
                ('qq', models.CharField(default='', max_length=20)),
                ('vx', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=200)),
                ('news_name', models.CharField(default='', max_length=200)),
                ('news_url', models.CharField(default='', max_length=200)),
            ],
        ),
    ]