# Generated by Django 5.0.7 on 2024-10-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_header', models.CharField(max_length=100)),
                ('img_update', models.ImageField(upload_to='/media')),
                ('description_of_the_update', models.TextField()),
            ],
        ),
    ]
