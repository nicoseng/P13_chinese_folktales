# Generated by Django 4.1.5 on 2023-02-27 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese_folktales_website', '0015_alter_story_textfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='images',
        ),
        migrations.AddField(
            model_name='story',
            name='bg_image',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='audiofile',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]