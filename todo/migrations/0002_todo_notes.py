# Generated by Django 5.0.1 on 2024-01-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='notes',
            field=models.CharField(default='scrie aici', max_length=255),
            preserve_default=False,
        ),
    ]
