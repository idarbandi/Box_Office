# Generated by Django 4.0 on 2022-10-10 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieCrawl', '0006_genremovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actormovie',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='actorsmovies', to='MovieCrawl.movie'),
        ),
        migrations.CreateModel(
            name='MovieImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='MovieImages/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='MovieCrawl.movie')),
            ],
        ),
    ]
