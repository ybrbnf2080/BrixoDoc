# Generated by Django 4.0.3 on 2022-08-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0014_rename_ref_name_ref203_ref_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacture203',
            old_name='short_no',
            new_name='short_name',
        ),
    ]
