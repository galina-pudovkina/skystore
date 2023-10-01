# Generated by Django 4.2.5 on 2023-10-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='содержимое')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='изображение')),
                ('issued_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
            ],
        ),
    ]
