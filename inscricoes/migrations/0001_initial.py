# Generated by Django 4.1.5 on 2023-02-09 23:52

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data_publicacao', models.DateTimeField(verbose_name=datetime.datetime(2023, 2, 9, 23, 52, 55, 205968, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
