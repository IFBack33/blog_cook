# Generated by Django 4.2.7 on 2023-11-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
