# Generated by Django 4.1.5 on 2023-03-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese_folktales_website', '0026_rename_level_level_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='level',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
