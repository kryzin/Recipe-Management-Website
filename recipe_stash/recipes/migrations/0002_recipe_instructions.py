# Generated by Django 4.1.12 on 2023-10-25 17:30

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=markdownx.models.MarkdownxField(null=True),
        ),
    ]
