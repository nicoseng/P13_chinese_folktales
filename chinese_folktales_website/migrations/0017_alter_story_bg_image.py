# Generated by Django 4.1.5 on 2023-02-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese_folktales_website', '0016_remove_story_images_story_bg_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='bg_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
