# Generated by Django 2.2.1 on 2019-05-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_content_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_md',
            field=models.BooleanField(default=True, verbose_name='markdown语法'),
        ),
    ]
