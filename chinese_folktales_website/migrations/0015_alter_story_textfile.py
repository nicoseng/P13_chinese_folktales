# Generated by Django 4.1.5 on 2023-02-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese_folktales_website', '0014_alter_story_audiofile_alter_story_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='textfile',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
