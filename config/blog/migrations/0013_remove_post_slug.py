# Generated by Django 5.0.3 on 2024-03-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
