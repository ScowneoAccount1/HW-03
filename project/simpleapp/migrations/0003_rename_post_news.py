# Generated by Django 4.1.1 on 2022-11-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
    ]