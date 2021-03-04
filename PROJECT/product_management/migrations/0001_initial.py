# Generated by Django 3.1.5 on 2021-02-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('brand', models.CharField(default='', max_length=20)),
                ('inStock', models.BooleanField(default='True')),
                ('description', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(upload_to='uploads/products/images/')),
            ],
        ),
    ]