# Generated by Django 4.1.2 on 2022-11-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfgdfg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
