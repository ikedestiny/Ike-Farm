# Generated by Django 4.1.7 on 2023-03-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0006_alter_stock_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
