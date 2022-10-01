# Generated by Django 4.0 on 2022-09-30 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('year', models.PositiveIntegerField(choices=[(1, 'Integer'), (2, 'String'), (3, 'Float')], default=1)),
                ('age_res', models.CharField(max_length=10)),
                ('summary', models.TextField(blank=True)),
                ('awards', models.CharField(max_length=32)),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='actrs_movies', to='MovieCrawl.actor')),
                ('director_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='MovieCrawl.director')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='MovieCrawl.genre')),
            ],
        ),
        migrations.CreateModel(
            name='DirMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='directors', to='MovieCrawl.director')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='directorsmovies', to='MovieCrawl.movie')),
            ],
        ),
        migrations.CreateModel(
            name='ActorMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='moviesactors', to='MovieCrawl.actor')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atorsmovies', to='MovieCrawl.movie')),
            ],
        ),
    ]
