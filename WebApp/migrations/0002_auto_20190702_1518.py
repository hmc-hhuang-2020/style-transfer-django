# Generated by Django 2.1.9 on 2019-07-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]