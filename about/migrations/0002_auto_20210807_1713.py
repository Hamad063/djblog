# Generated by Django 3.2.5 on 2021-08-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='contenr',
            new_name='content',
        ),
    ]