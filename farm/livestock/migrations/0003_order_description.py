# Generated by Django 4.1.7 on 2023-03-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0002_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Description',
            field=models.CharField(default='Please describe your order here', max_length=1000),
            preserve_default=False,
        ),
    ]