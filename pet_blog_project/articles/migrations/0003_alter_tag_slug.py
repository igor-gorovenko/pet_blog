# Generated by Django 4.2.2 on 2023-06-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_tag_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
