# Generated by Django 4.0 on 2022-11-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=4000)),
                ('image', models.ImageField(upload_to='media/blogs/')),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]
