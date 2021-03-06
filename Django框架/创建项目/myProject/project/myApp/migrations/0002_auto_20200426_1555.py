# Generated by Django 3.0.5 on 2020-04-26 07:55

from django.db import migrations, models
import django.db.models.manager
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterModelManagers(
            name='students',
            managers=[
                ('stuObj', django.db.models.manager.Manager()),
            ],
        ),
    ]
