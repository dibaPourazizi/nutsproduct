# Generated by Django 4.2.2 on 2023-06-30 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cityId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.city'),
            preserve_default=False,
        ),
    ]
