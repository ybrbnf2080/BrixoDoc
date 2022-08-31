# Generated by Django 4.0.3 on 2022-08-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0016_alter_vehicles_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article200',
            name='art_stat',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='ArtStat'),
        ),
        migrations.AlterField(
            model_name='article200',
            name='gen_art_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='GenArtNo'),
        ),
        migrations.AlterField(
            model_name='article200',
            name='gtin',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='GTIN'),
        ),
        migrations.AlterField(
            model_name='article200',
            name='quant_per_unit',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='QuantPerUnit'),
        ),
        migrations.AlterField(
            model_name='article200',
            name='quant_unit',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='QuantUnit'),
        ),
        migrations.AlterField(
            model_name='article200',
            name='status_dat',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='StatusDat'),
        ),
        migrations.AlterField(
            model_name='critval210',
            name='crit_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='CritNo'),
        ),
        migrations.AlterField(
            model_name='doc231and232',
            name='doc_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='DocNo'),
        ),
        migrations.AlterField(
            model_name='doc231and232',
            name='doc_term_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='DocTermNorm'),
        ),
        migrations.AlterField(
            model_name='doc231and232',
            name='doc_type',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='DocContentType'),
        ),
        migrations.AlterField(
            model_name='doc231and232',
            name='doc_type_one',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='DocTermNorm'),
        ),
        migrations.AlterField(
            model_name='doc231and232',
            name='lang_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LangNo'),
        ),
        migrations.AlterField(
            model_name='lnk400',
            name='gen_art_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='GenArtNo'),
        ),
        migrations.AlterField(
            model_name='lnk400',
            name='lnk_target_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LnkTargetNo'),
        ),
        migrations.AlterField(
            model_name='lnk400',
            name='lnk_target_type',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LnkTargetType'),
        ),
        migrations.AlterField(
            model_name='lnk400',
            name='seq_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='SeqNo'),
        ),
        migrations.AlterField(
            model_name='manufacture203',
            name='man_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='ManNo'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='adr_type',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Adr Type'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='brand_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Brand No'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='data_release',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Data Release'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='doc_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Doc No'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='doc_type',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='DocType'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='full',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Full'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='man_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Man No'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='ref_data_version',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='ref_data_version'),
        ),
        migrations.AlterField(
            model_name='suppliers200',
            name='version_date',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Version Date'),
        ),
        migrations.AlterField(
            model_name='table404',
            name='gen_art_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='GenArtNo'),
        ),
        migrations.AlterField(
            model_name='table404',
            name='lnk_target_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LnkTargetNo'),
        ),
        migrations.AlterField(
            model_name='table404',
            name='lnk_target_type',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LnkTargetType'),
        ),
        migrations.AlterField(
            model_name='table404',
            name='sort_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='sort_no'),
        ),
        migrations.AlterField(
            model_name='table410',
            name='first_page',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='FirstPage'),
        ),
        migrations.AlterField(
            model_name='table410',
            name='gen_art_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='GenArtNo'),
        ),
        migrations.AlterField(
            model_name='table410',
            name='lnk_target_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LnkTargetNo'),
        ),
        migrations.AlterField(
            model_name='table410',
            name='lnk_target_type',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='LnkTargetType'),
        ),
        migrations.AlterField(
            model_name='table410',
            name='seq_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='SeqNo'),
        ),
        migrations.AlterField(
            model_name='table410',
            name='sort_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='sort_no'),
        ),
        migrations.AlterField(
            model_name='trade207',
            name='first_page',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='FirstPage'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='veh_model_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='VEH_MODEL_NO'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='veh_type_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='VEH_TYPE_NO'),
        ),
    ]
