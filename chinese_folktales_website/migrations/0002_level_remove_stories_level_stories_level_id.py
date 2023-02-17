# Generated by Django 4.1.5 on 2023-02-06 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chinese_folktales_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stories',
            name='level',
        ),
        migrations.AddField(
            model_name='stories',
            name='level_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
