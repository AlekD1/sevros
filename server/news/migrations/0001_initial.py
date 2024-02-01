# Generated by Django 4.2.3 on 2023-11-18 20:06

from django.db import migrations, models
import mixins.path_mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
                ('description', models.CharField(db_index=True, max_length=255, verbose_name='Краткое описание для карточки')),
                ('image', models.ImageField(upload_to=mixins.path_mixins.make_dir_for_news_images, verbose_name='Изображение')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('tags', models.ManyToManyField(db_index=True, to='news.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]