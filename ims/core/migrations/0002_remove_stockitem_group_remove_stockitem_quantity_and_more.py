# Generated by Django 4.1.7 on 2023-02-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockitem',
            name='group',
        ),
        migrations.RemoveField(
            model_name='stockitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='stockitem',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
