# Generated by Django 2.2.2 on 2019-06-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190613_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditemdata',
            name='item_publisher',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='lostitemdata',
            name='item_publisher',
            field=models.CharField(default='', max_length=20),
        ),
    ]
