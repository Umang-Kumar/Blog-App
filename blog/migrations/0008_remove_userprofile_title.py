# Generated by Django 4.1.4 on 2023-02-16 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='title',
        ),
    ]
