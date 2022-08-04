# Generated by Django 4.0.3 on 2022-08-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0003_rename_crin_no_critname210_crit_no_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CritName210',
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='first_page',
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='sort_no',
        ),
        migrations.AddField(
            model_name='crit210',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='crit210',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
    ]