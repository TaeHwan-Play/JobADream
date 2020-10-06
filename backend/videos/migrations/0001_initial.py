# Generated by Django 3.1.2 on 2020-10-06 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angry', models.IntegerField(default=0)),
                ('disgusted', models.IntegerField(default=0)),
                ('fearful', models.IntegerField(default=0)),
                ('happy', models.IntegerField(default=0)),
                ('neutral', models.IntegerField(default=0)),
                ('sad', models.IntegerField(default=0)),
                ('surprised', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gaze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blinking', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
                ('right', models.IntegerField(default=0)),
                ('center', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HeadPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottom', models.IntegerField(default=0)),
                ('top', models.IntegerField(default=0)),
                ('right', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emotions', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='videos.emotion')),
                ('gaze', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='videos.gaze')),
                ('head', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='videos.headposition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
                ('video_file', models.FileField(blank=True, upload_to='videos')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.videoresult')),
                ('tag', models.ManyToManyField(blank=True, to='videos.Tag')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
