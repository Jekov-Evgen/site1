# Generated by Django 5.0.7 on 2024-10-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_gamepost_img_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepost',
            name='img_update',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
