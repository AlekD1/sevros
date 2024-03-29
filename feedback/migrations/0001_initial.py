# Generated by Django 4.2.3 on 2023-11-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=255, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_check', models.BooleanField(default=False, verbose_name='Проверено?')),
            ],
            options={
                'verbose_name': '"обратная связь"',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
