# Generated by Django 4.2.5 on 2023-09-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
