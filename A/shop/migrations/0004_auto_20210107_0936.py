# Generated by Django 3.0 on 2021-01-07 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='product',
        ),
    ]