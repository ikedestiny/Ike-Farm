# Generated by Django 4.1.7 on 2023-03-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0004_alter_order_order_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('unit_price', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to=None)),
                ('sold_out', models.BooleanField()),
            ],
        ),
    ]
