# Generated by Django 4.1.1 on 2022-09-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0036_remove_doc231and232_file_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc231and232',
            name='file_paths',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Sirius_McLine\\PycharmProjects\\BrixoDoc/ImportTAF/sources_tec/image/1070-0101.BMP'),
        ),
    ]