# Generated by Django 5.0.1 on 2024-02-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='media/images')),
            ],
        ),
    ]
