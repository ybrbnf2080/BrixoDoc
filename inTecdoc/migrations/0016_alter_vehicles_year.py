# Generated by Django 4.0.3 on 2022-08-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0015_alter_vehicles_body_type_alter_vehicles_ccm_tech_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='year',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='YEAR'),
        ),
    ]