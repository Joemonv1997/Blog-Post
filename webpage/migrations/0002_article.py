# Generated by Django 4.0 on 2021-12-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
