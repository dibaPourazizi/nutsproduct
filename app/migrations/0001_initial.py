# Generated by Django 4.2.2 on 2023-06-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=200)),
                ('discounted_price', models.FloatField()),
                ('quantity', models.FloatField(max_length=200)),
                ('type', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('AJ', 'آجیل'), ('KH', 'خشکبار'), ('ZA', 'زعفران')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
