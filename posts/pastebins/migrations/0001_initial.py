# Generated by Django 2.2 on 2019-06-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pastebins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('private', models.BooleanField(null=True)),
                ('public', models.BooleanField(null=True)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]