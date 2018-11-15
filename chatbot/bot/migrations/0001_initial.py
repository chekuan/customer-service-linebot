# Generated by Django 2.0.1 on 2018-01-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('brief_intro', models.TextField()),
                ('duration', models.TextField()),
                ('requirements', models.TextField()),
                ('qualification', models.TextField()),
                ('details', models.TextField()),
                ('notice', models.TextField()),
            ],
        ),
    ]
