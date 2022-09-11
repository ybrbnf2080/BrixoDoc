# Generated by Django 4.1.1 on 2022-09-05 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0018_chanks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article200',
            name='supers_id',
        ),
        migrations.AddField(
            model_name='supers204',
            name='art_no_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inTecdoc.article200', verbose_name='ArtNo'),
        ),
    ]