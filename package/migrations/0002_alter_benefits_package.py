# Generated by Django 4.0 on 2022-10-24 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefits',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='package.package'),
        ),
    ]