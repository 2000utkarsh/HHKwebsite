# Generated by Django 2.1.5 on 2019-01-31 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='roll_no',
        ),
    ]