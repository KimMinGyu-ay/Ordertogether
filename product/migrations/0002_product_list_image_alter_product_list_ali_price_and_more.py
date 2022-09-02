# Generated by Django 4.1 on 2022-09-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_list',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='ali_price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='name',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='ot_price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterModelTable(
            name='product_list',
            table='Product_list',
        ),
    ]