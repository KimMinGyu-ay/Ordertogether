# Generated by Django 4.1 on 2022-09-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
