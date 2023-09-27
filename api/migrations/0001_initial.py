# Generated by Django 4.2.5 on 2023-09-27 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/about')),
                ('text', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='FeedbackPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField(max_length=50, null=True)),
                ('user_agreement', models.FileField(blank=True, null=True, upload_to='user_agreements/')),
                ('company_description', models.TextField(max_length=250, null=True)),
                ('icons', models.ImageField(upload_to='media/icons')),
            ],
            options={
                'verbose_name_plural': 'Хедер',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField(max_length=50, null=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('icons', models.ImageField(upload_to='media/icons')),
            ],
            options={
                'verbose_name_plural': 'Хедер',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/services/reviews')),
                ('text', models.CharField(max_length=500, null=True)),
                ('FIO', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('sub_title', models.CharField(max_length=255, null=True)),
                ('slide_order', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='StaticText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, null=True)),
                ('Is_Active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Текст на сайте',
            },
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=450, null=True)),
                ('description', models.TextField(max_length=450, null=True)),
                ('slide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_blocks', to='api.slide')),
            ],
            options={
                'verbose_name_plural': 'Текст',
            },
        ),
        migrations.CreateModel(
            name='SlideMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('sub_title', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(max_length=450, null=True)),
                ('image', models.ImageField(upload_to='media/photo')),
                ('page_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_slide', to='api.header')),
            ],
            options={
                'verbose_name_plural': 'Гланый слайд',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/images')),
                ('slide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='api.slide')),
            ],
            options={
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='IconMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_logo', models.URLField(null=True)),
                ('page_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icon_slide', to='api.header')),
            ],
            options={
                'verbose_name_plural': 'Иконки',
            },
        ),
    ]