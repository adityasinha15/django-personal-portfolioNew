# Generated by Django 3.0.6 on 2020-07-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_project_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='portfolio/image/'),
        ),
    ]
