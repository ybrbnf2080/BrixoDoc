# Generated by Django 4.0.3 on 2022-08-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0006_remove_ref_203_artnoid_article_200_refnoid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_200',
            name='GenArtNoId',
        ),
        migrations.AddField(
            model_name='article_200',
            name='GenArtNo',
            field=models.IntegerField(blank=True, null=True, verbose_name='GenArtNo'),
        ),
        migrations.DeleteModel(
            name='GenArt_211',
        ),
    ]
