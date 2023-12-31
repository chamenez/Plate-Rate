# Generated by Django 4.2.6 on 2023-11-14 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_restaurant_name_alter_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='content.restaurant'),
        ),
        migrations.AddField(
            model_name='dish',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='slug',
            field=models.CharField(default='', max_length=255),
        ),
    ]
