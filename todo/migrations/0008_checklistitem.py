# Generated by Django 5.0.1 on 2024-01-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_delete_newview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
