# Generated by Django 3.1.7 on 2021-03-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20210323_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='type',
            new_name='content_type',
        ),
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.FileField(default=1, upload_to='content'),
            preserve_default=False,
        ),
    ]