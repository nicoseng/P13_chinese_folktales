# Generated by Django 4.1.5 on 2023-02-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese_folktales_website', '0018_alter_story_audiofile_alter_story_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='audiofile',
            field=models.FileField(upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='story',
            name='bg_image',
            field=models.FileField(upload_to='bg_image'),
        ),
    ]