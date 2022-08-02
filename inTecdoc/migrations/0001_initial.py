# Generated by Django 4.0.3 on 2022-08-02 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_200',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GTIN', models.IntegerField(blank=True, null=True, verbose_name='GTIN')),
                ('ArtNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='ArtNo')),
                ('QuantUnit', models.IntegerField(blank=True, null=True, verbose_name='QuantUnit')),
                ('QuantPerUnit', models.IntegerField(blank=True, null=True, verbose_name='QuantPerUnit')),
                ('ArtStat', models.IntegerField(blank=True, null=True, verbose_name='ArtStat')),
                ('StatusDat', models.IntegerField(blank=True, null=True, verbose_name='StatusDat')),
            ],
        ),
        migrations.CreateModel(
            name='CritName_210',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CritNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='CrtNo')),
                ('CritName', models.CharField(blank=True, max_length=255, null=True, verbose_name='CrtName')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='GenArt_211',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GenArtNo', models.IntegerField(blank=True, null=True, verbose_name='GenArtNo')),
                ('ArtNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='ArtNo')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture_203',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ManNo', models.IntegerField(blank=True, null=True, verbose_name='ManNo')),
                ('ShortName', models.CharField(blank=True, max_length=255, null=True, verbose_name='ShortName')),
                ('TermPlain', models.CharField(blank=True, max_length=255, null=True, verbose_name='TermPlain')),
            ],
        ),
        migrations.CreateModel(
            name='Supliers_200',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('BrandNo', models.IntegerField(blank=True, null=True, verbose_name='BrandNo')),
            ],
        ),
        migrations.CreateModel(
            name='Trade_207',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TradeNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='TradeNo')),
                ('FirstPage', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoTrade_207', to='inTecdoc.article_200')),
            ],
        ),
        migrations.CreateModel(
            name='Table_410',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LnkTargetType', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('LnkTargetNo', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('SeqNo', models.IntegerField(blank=True, null=True, verbose_name='SeqNo')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('CritNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritNo')),
                ('CritVal', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritVal')),
                ('FirstPage', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoTable_410', to='inTecdoc.article_200')),
            ],
        ),
        migrations.CreateModel(
            name='Table_404',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LnkTargetType', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('LnkTargetNo', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoTable_404', to='inTecdoc.article_200')),
            ],
        ),
        migrations.CreateModel(
            name='Supers_204',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupersNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='SupersNo')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoSupers_204', to='inTecdoc.article_200')),
            ],
        ),
        migrations.CreateModel(
            name='Ref_203',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RefNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='RefNo')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoRef_203', to='inTecdoc.article_200')),
                ('ManNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ManNoRef_203', to='inTecdoc.manufacture_203')),
            ],
        ),
        migrations.CreateModel(
            name='Lnk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LnkTargetNo', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('LnkTargetType', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('SeqNo', models.IntegerField(blank=True, null=True, verbose_name='SeqNo')),
                ('ArtNo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoLnk', to='inTecdoc.article_200')),
            ],
        ),
        migrations.CreateModel(
            name='Doc_231_232',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocNo', models.IntegerField(blank=True, null=True, verbose_name='DocNo')),
                ('LangNo', models.IntegerField(blank=True, null=True, verbose_name='LangNo')),
                ('DocName', models.CharField(blank=True, max_length=255, null=True, verbose_name='DocName')),
                ('DocContentType', models.IntegerField(blank=True, null=True, verbose_name='DocContentType')),
                ('DocTermNorm', models.IntegerField(blank=True, null=True, verbose_name='DocTermNorm')),
                ('DocType', models.IntegerField(blank=True, null=True, verbose_name='DocType')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoDoc_231_232', to='inTecdoc.article_200')),
            ],
        ),
        migrations.CreateModel(
            name='Crit_210',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CritVal', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritVal')),
                ('FirstPage', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoCrit_210', to='inTecdoc.article_200')),
                ('CritNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CritNoCrit_210', to='inTecdoc.critname_210')),
            ],
        ),
        migrations.CreateModel(
            name='Country_202',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryCode', models.CharField(blank=True, max_length=255, null=True, verbose_name='CountryCode')),
                ('CountryName', models.CharField(blank=True, max_length=255, null=True, verbose_name='CountryName')),
                ('ArtNoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtNoCountry_202', to='inTecdoc.article_200')),
            ],
        ),
        migrations.AddField(
            model_name='article_200',
            name='BrandNoId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BrandNoArticle_200', to='inTecdoc.supliers_200'),
        ),
        migrations.AddField(
            model_name='article_200',
            name='GenArtNoId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GenArtNoArticle_200', to='inTecdoc.genart_211'),
        ),
    ]
