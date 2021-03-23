# Generated by Django 3.1.7 on 2021-03-23 12:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20210323_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.FileField(upload_to='content', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'mp4'])]),
        ),
    ]