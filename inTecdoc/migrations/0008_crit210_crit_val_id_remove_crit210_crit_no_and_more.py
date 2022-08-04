# Generated by Django 4.0.3 on 2022-08-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0007_remove_critval210_crit_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='crit210',
            name='crit_val_id',
            field=models.ManyToManyField(blank=True, related_name='CritNoId', to='inTecdoc.critval210'),
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='crit_no',
        ),
        migrations.AddField(
            model_name='crit210',
            name='crit_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='CritNo'),
        ),
    ]