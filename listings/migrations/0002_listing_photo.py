# Generated by Django 2.1.5 on 2019-02-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo',
            field=models.ImageField(default=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]