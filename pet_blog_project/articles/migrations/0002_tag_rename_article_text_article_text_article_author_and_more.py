# Generated by Django 4.2.2 on 2023-06-17 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Enter a tag", max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name="article",
            old_name="article_text",
            new_name="text",
        ),
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="articles.author",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="creation_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(help_text="Select a tag", to="articles.tag"),
        ),
    ]