# Generated by Django 4.0.3 on 2022-08-03 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article200',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_art_no', models.IntegerField(blank=True, null=True, verbose_name='GenArtNo')),
                ('gtin', models.IntegerField(blank=True, null=True, verbose_name='GTIN')),
                ('art_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='ArtNo')),
                ('quant_unit', models.IntegerField(blank=True, null=True, verbose_name='QuantUnit')),
                ('quant_per_unit', models.IntegerField(blank=True, null=True, verbose_name='QuantPerUnit')),
                ('art_stat', models.IntegerField(blank=True, null=True, verbose_name='ArtStat')),
                ('status_dat', models.IntegerField(blank=True, null=True, verbose_name='StatusDat')),
            ],
        ),
        migrations.CreateModel(
            name='Country202',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='CountryCode')),
                ('country_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='CountryName')),
            ],
        ),
        migrations.CreateModel(
            name='CritName210',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crin_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='CrtNo')),
                ('crit_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='CrtName')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture203',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_no', models.IntegerField(blank=True, null=True, verbose_name='ManNo')),
                ('short_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='ShortName')),
                ('term_plain', models.CharField(blank=True, max_length=255, null=True, verbose_name='TermPlain')),
            ],
        ),
        migrations.CreateModel(
            name='Supers204',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supers_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='SupersNo')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers200',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('brand_no', models.IntegerField(blank=True, null=True, verbose_name='BrandNo')),
            ],
        ),
        migrations.CreateModel(
            name='Trade207',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='TradeNo')),
                ('first_page', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('art_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoTrade_207', to='inTecdoc.article200')),
            ],
        ),
        migrations.CreateModel(
            name='Table410',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lnk_target_type', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('lnk_target_no', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('seq_no', models.IntegerField(blank=True, null=True, verbose_name='SeqNo')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('crit_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritNo')),
                ('crit_val', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritVal')),
                ('first_page', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('art_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoTable_410', to='inTecdoc.article200')),
            ],
        ),
        migrations.CreateModel(
            name='Table404',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lnk_target_type', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('lnk_target_no', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('art_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoTable_404', to='inTecdoc.article200')),
            ],
        ),
        migrations.CreateModel(
            name='Ref203',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='RefNo')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('man_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ManNoRef_203', to='inTecdoc.manufacture203')),
            ],
        ),
        migrations.CreateModel(
            name='Lnk400',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lnk_target_no', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('lnk_target_type', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('seq_no', models.IntegerField(blank=True, null=True, verbose_name='SeqNo')),
                ('art_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoLnk', to='inTecdoc.article200')),
            ],
        ),
        migrations.CreateModel(
            name='Doc231and232',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_no', models.IntegerField(blank=True, null=True, verbose_name='DocNo')),
                ('lang_no', models.IntegerField(blank=True, null=True, verbose_name='LangNo')),
                ('doc_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='DocName')),
                ('doc_content_type', models.IntegerField(blank=True, null=True, verbose_name='DocContentType')),
                ('doc_term_no', models.IntegerField(blank=True, null=True, verbose_name='DocTermNorm')),
                ('doc_type', models.IntegerField(blank=True, null=True, verbose_name='DocType')),
                ('art_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoDoc_231_232', to='inTecdoc.article200')),
            ],
        ),
        migrations.CreateModel(
            name='Crit210',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crit_val', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritVal')),
                ('first_page', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('sort_no', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('art_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoCrit_210', to='inTecdoc.article200')),
                ('crit_no_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CritNoCrit_210', to='inTecdoc.critname210')),
            ],
        ),
        migrations.AddField(
            model_name='article200',
            name='brand_no_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_no_article', to='inTecdoc.suppliers200'),
        ),
        migrations.AddField(
            model_name='article200',
            name='country',
            field=models.ManyToManyField(blank=True, related_name='CountryArticle_200', to='inTecdoc.country202'),
        ),
        migrations.AddField(
            model_name='article200',
            name='ref_no_id',
            field=models.ManyToManyField(blank=True, related_name='ref_no_article', to='inTecdoc.ref203'),
        ),
        migrations.AddField(
            model_name='article200',
            name='supers_id',
            field=models.ManyToManyField(blank=True, null=True, related_name='supers_article', to='inTecdoc.supers204'),
        ),
    ]
