# Generated by Django 3.1.7 on 2021-04-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazonWeb', '0002_auto_20210414_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='track_id',
            field=models.IntegerField(default=1),
        ),
    ]
