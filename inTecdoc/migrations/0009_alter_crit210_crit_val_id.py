# Generated by Django 4.0.3 on 2022-08-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0008_crit210_crit_val_id_remove_crit210_crit_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crit210',
            name='crit_val_id',
            field=models.ManyToManyField(blank=True, to='inTecdoc.critval210', verbose_name='CritVal'),
        ),
    ]