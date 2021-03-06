# Generated by Django 2.1.5 on 2019-01-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_auto_20190131_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='subject',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
