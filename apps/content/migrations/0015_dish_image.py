# Generated by Django 4.2.6 on 2023-11-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_alter_dish_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dish_images/'),
        ),
    ]
