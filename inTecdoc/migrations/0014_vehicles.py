# Generated by Django 4.0.3 on 2022-08-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0013_alter_ref203_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veh_type_no', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('veh_model_no', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('veh_brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('veh_model_intl', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('veh_type_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('engine_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('body_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('drive_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('engine_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('values_per_chamber', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('cylinders', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('litres', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('ccm_tech', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('fuel_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('fuel_mixture_formation', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('hp', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('kw', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
            ],
        ),
    ]
