# Generated by Django 4.1.1 on 2022-09-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0042_alter_doc231and232_file_paths'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc231and232',
            name='file_field',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='file_field'),
        ),
    ]
