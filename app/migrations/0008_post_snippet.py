# Generated by Django 4.2.5 on 2023-10-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read Blog Post', max_length=255),
        ),
    ]
