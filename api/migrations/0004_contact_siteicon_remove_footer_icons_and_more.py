# Generated by Django 4.2.5 on 2023-09-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_textblock_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='SiteIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/icons/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='icons',
        ),
        migrations.RemoveField(
            model_name='header',
            name='icons',
        ),
        migrations.DeleteModel(
            name='SlideMain',
        ),
        migrations.AddField(
            model_name='footer',
            name='icons',
            field=models.ManyToManyField(blank=True, related_name='headers', to='api.siteicon'),
        ),
        migrations.AddField(
            model_name='header',
            name='icons',
            field=models.ManyToManyField(blank=True, related_name='footer_icons', to='api.siteicon'),
        ),
    ]