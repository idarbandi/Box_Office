# Generated by Django 4.0 on 2022-10-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributer',
            name='web',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
