# Generated by Django 3.1.2 on 2020-10-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_remove_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('1', 'VILLA BOR'), ('2', 'VILLA ASPEN'), ('3', 'VILLA ELA')], max_length=50),
        ),
    ]
