# Generated by Django 5.0.4 on 2024-04-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_picture01_smartphone_pictureback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='manufacturer',
            field=models.CharField(choices=[('Apple', 'Apple'), ('Samsung', 'Samsung'), ('Google', 'Google'), ('Sony', 'Sony'), ('Xiaomi', 'Xiaomi'), ('Huawei', 'Huawei')], max_length=8),
        ),
    ]
