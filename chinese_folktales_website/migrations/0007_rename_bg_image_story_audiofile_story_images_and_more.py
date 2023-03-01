# Generated by Django 4.1.5 on 2023-02-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese_folktales_website', '0006_story_bg_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='bg_image',
            new_name='audiofile',
        ),
        migrations.AddField(
            model_name='story',
            name='images',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='textfile',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]