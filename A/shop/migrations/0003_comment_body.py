# Generated by Django 3.0 on 2021-01-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=400, null=True),
        ),
    ]