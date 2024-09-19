# Generated by Django 4.2.16 on 2024-09-19 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanctuary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanct_name', models.CharField(max_length=200)),
                ('sanct_address', models.TextField()),
                ('sanct_postcode', models.CharField(max_length=15, unique=True)),
                ('sanct_telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('sanct_email', models.EmailField(max_length=254)),
                ('sanct_website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('excerpt', models.TextField(blank=True)),
                ('dog_name', models.CharField(max_length=200, unique=True)),
                ('dog_type', models.CharField(max_length=200, unique=True)),
                ('dog_age', models.IntegerField()),
                ('dog_stay', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('sanctuary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='blog.sanctuary')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]
