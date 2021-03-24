# Generated by Django 3.1.7 on 2021-03-24 09:57

import Bookord.user.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='friends',
            new_name='followings',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to=Bookord.user.models.user_directory_path),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=200)),
                ('page_number', models.PositiveIntegerField()),
                ('score', models.PositiveIntegerField()),
                ('additional_info', models.TextField()),
                ('overview', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(to='user.Book'),
        ),
    ]