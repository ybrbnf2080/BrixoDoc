from django.db import models
from django.conf import settings

BASE_DIR = settings.BASE_DIR
import os


class Suppliers200(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)  # Имя BranNo
    brand_no = models.BigIntegerField(verbose_name="Brand No", blank=True, null=True)  # BranNo
    street = models.CharField(max_length=255, verbose_name="Street", blank=True, null=True)  # Street1 40
    street_two = models.CharField(max_length=255, verbose_name="Street2", blank=True, null=True)  # Street2 40
    country_code = models.CharField(max_length=255, verbose_name="Country Code", blank=True,
                                    null=True)  # CountryCode 40 PostCode
    post_code = models.CharField(max_length=255, verbose_name="Post Code", blank=True, null=True)  # PostCode 40
    city = models.CharField(max_length=255, verbose_name="City", blank=True, null=True)  # City1 40
    phone = models.CharField(max_length=255, verbose_name="Phone", blank=True, null=True)  # Phone 40
    email = models.CharField(max_length=255, verbose_name="Email", blank=True, null=True)  # Email 40
    web_site = models.CharField(max_length=255, verbose_name="Web", blank=True, null=True)  # WEB 40
    adr_type = models.BigIntegerField(verbose_name="Adr Type", blank=True, null=True)  # AdrType 40
    doc_no = models.BigIntegerField(verbose_name="Doc No", blank=True, null=True)  # DocNo 42
    doc_type = models.BigIntegerField(verbose_name="DocType", blank=True, null=True)  # DocType 42
    data_release = models.BigIntegerField(verbose_name="Data Release", blank=True, null=True)
    version_date = models.BigIntegerField(verbose_name="Version Date", blank=True, null=True)
    man_no = models.BigIntegerField(verbose_name="Man No", blank=True, null=True)
    full = models.BigIntegerField(verbose_name="Full", blank=True, null=True)
    term1 = models.CharField(max_length=255, verbose_name="Term1", blank=True, null=True)
    ref_data_version = models.BigIntegerField(verbose_name="ref_data_version", blank=True, null=True)
    post_code_pobox = models.CharField(max_length=255, verbose_name="post_code_pobox", blank=True, null=True)
    post_code_cus = models.CharField(max_length=255, verbose_name="post_code_cus", blank=True, null=True)

    # class Meta:
    #     verbose_name = """Производитель комплектующей"""
    #     verbose_name_plural = """Производители комплектующих"""

    def __str__(self):
        return self.name


class Country202(models.Model):
    country_code = models.CharField(max_length=255, verbose_name="CountryCode", blank=True, null=True)  # Код страны
    country_name = models.CharField(max_length=255, verbose_name="CountryName", blank=True, null=True)  # Имя страны

    class Meta:
        verbose_name = """Страна"""
        verbose_name_plural = """Страны"""
        default_related_name = 'country'

    def __str__(self):
        return self.country_code


class Manufacture203(models.Model):
    man_no = models.BigIntegerField(verbose_name="ManNo", blank=True, null=True)  # BrandNo
    short_name = models.CharField(max_length=255, verbose_name="ShortName", blank=True, null=True)  # ShortName
    term_plain = models.CharField(max_length=255, verbose_name="TermPlain", blank=True, null=True)  # TermPlain

    # class Meta:
    #     verbose_name = """Производитель авто"""
    #     verbose_name_plural = """Производители авто"""

    def __str__(self):
        return self.short_name


# BASE_DIR = 'C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/'


class Doc231and232(models.Model):
    doc_no = models.BigIntegerField(verbose_name="DocNo", blank=True, null=True)  # DocNo 231
    doc_name = models.CharField(max_length=255, verbose_name="DocName", blank=True, null=True)  # DocName 231
    lang_no = models.BigIntegerField(verbose_name="LangNo", blank=True, null=True)  # LangNo 231
    doc_type = models.BigIntegerField(verbose_name="DocContentType", blank=True, null=True)  # DocContentType 231
    doc_term_no = models.BigIntegerField(verbose_name="DocTermNorm", blank=True, null=True)  # DocTermNorm 231
    doc_type_one = models.BigIntegerField(verbose_name="DocTermNorm", blank=True, null=True)  # DocType 231

    # class Meta:
    #     verbose_name = """Документ"""
    #     verbose_name_plural = """Документы"""

    def __str__(self):
        return self.doc_name


class Article200(models.Model):
    art_no = models.CharField(max_length=255, verbose_name="ArtNo", blank=True, null=True)  # ArtNo 200
    country_id = models.ManyToManyField(Country202, blank=True, related_name='CountryArticle_200')  # CountryCode 202
    gen_art_no = models.BigIntegerField(verbose_name="GenArtNo", blank=True, null=True)  # GenArtNo 211
    brand_no_id = models.ForeignKey(Suppliers200, on_delete=models.CASCADE, related_name='brand_no_article', blank=True,
                                    null=True)  # BrandNo
    gtin = models.BigIntegerField(verbose_name="GTIN", blank=True, null=True)  # GTIN 209
    quant_unit = models.BigIntegerField(verbose_name="QuantUnit", blank=True, null=True)  # QuantUnit 212
    quant_per_unit = models.BigIntegerField(verbose_name="QuantPerUnit", blank=True, null=True)  # QuantPerUnit 212
    art_stat = models.BigIntegerField(verbose_name="ArtStat", blank=True, null=True)  # ArtStat 212
    status_dat = models.BigIntegerField(verbose_name="StatusDat", blank=True, null=True)  # StatusDat 212
    doc_no_id = models.ManyToManyField(Doc231and232, blank=True, related_name='doc_no_article')  # DocNo 232

    # class Meta:
    #     verbose_name = """Артикул"""
    #     verbose_name_plural = """Артикулы"""

    def __str__(self):
        return self.art_no


class Supers204(models.Model):
    supers_no = models.CharField(max_length=255, verbose_name="SupersNo", blank=True, null=True)  # SupersNo204
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, verbose_name='ArtNo', blank=True,
                                  null=True)  # ArtNo 203

    def __str__(self):
        return self.supers_no


class Ref203(models.Model):
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, verbose_name='ArtNo', blank=True,
                                  null=True)  # ArtNo 203
    man_no_id = models.ForeignKey(Manufacture203, on_delete=models.CASCADE, verbose_name='ManNoName', blank=True,
                                  null=True)  # ManNo 203
    ref_no = models.CharField(max_length=255, verbose_name="RefNo", blank=True, null=True)  # RefNo 203
    country_code_id = models.ForeignKey(Country202, on_delete=models.CASCADE, verbose_name='country_code', blank=True,
                                        null=True)  # CountryCode 203

    # class Meta:
    #     verbose_name = """Комплектующая от производителя авто"""
    #     verbose_name_plural = """Комплектующие от производителя авто"""

    def __str__(self):
        return self.ref_no


class CritVal210(models.Model):
    crit_no = models.BigIntegerField(verbose_name="CritNo", blank=True, null=True)  # Code
    name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)  # Name
    description = models.TextField(verbose_name="Description", blank=True, null=True)  # Comment

    # class Meta:
    #     verbose_name = """Список критерий"""
    #     verbose_name_plural = """Список критерий"""

    def __str__(self):
        return self.name


class Crit210(models.Model):
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, verbose_name="ArtNo", blank=True,
                                  null=True)  # ArtNo 210
    crit_no_id = models.ForeignKey(CritVal210, on_delete=models.CASCADE, verbose_name="CritNo", blank=True,
                                   null=True)  # CritNo 210
    crit_val = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)  # CritVal 210

    # class Meta:
    #     verbose_name = """Критерии комплектующего"""
    #     verbose_name_plural = """Критерии комплектующих"""

    def __str__(self):
        return self.crit_val


class Trade207(models.Model):
    trade_no = models.CharField(max_length=255, verbose_name="TradeNo", blank=True, null=True)  # TradeNo
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, related_name='ArtNoTrade_207', blank=True,
                                  null=True)  # ArtNo 210
    first_page = models.BigIntegerField(verbose_name="FirstPage", blank=True, null=True)  # FirstPage

    def __str__(self):
        return self.trade_no


class Vehicles(models.Model):
    veh_type_no = models.BigIntegerField(verbose_name="VEH_TYPE_NO", blank=True, null=True)
    veh_model_no = models.BigIntegerField(verbose_name="VEH_MODEL_NO", blank=True, null=True)
    veh_brand = models.CharField(max_length=255, verbose_name="VEH_BRAND", blank=True, null=True)
    veh_model_intl = models.CharField(max_length=255, verbose_name="VEH_MODEL_INTL", blank=True, null=True)
    veh_type_name = models.CharField(max_length=255, verbose_name="VEH_TYPE_NAME", blank=True, null=True)
    engine_code = models.CharField(max_length=255, verbose_name="ENGINE_CODE", blank=True, null=True)
    year = models.CharField(max_length=255, verbose_name="YEAR", blank=True, null=True)
    body_type = models.CharField(max_length=255, verbose_name="BODY_TYPE", blank=True, null=True)
    drive_type = models.CharField(max_length=255, verbose_name="DRIVE_TYPE", blank=True, null=True)
    engine_type = models.CharField(max_length=255, verbose_name="ENGINE_TYPE", blank=True, null=True)
    values_per_chamber = models.CharField(max_length=255, verbose_name="VALVES_PER_CHAMBER", blank=True, null=True)
    cylinders = models.CharField(max_length=255, verbose_name="CYLINDERS", blank=True, null=True)
    litres = models.CharField(max_length=255, verbose_name="LITRES", blank=True, null=True)
    ccm_tech = models.CharField(max_length=255, verbose_name="CCM_TECH", blank=True, null=True)
    fuel_type = models.CharField(max_length=255, verbose_name="FUEL_TYPE", blank=True, null=True)
    fuel_mixture_formation = models.CharField(max_length=255, verbose_name="FUEL_MIXTURE_FORMATION", blank=True,
                                              null=True)
    hp = models.CharField(max_length=255, verbose_name="HP", blank=True, null=True)
    kw = models.CharField(max_length=255, verbose_name="KW", blank=True, null=True)

    def __str__(self):
        return self.veh_brand


class Lnk400(models.Model):
    art_no_id = models.ForeignKey(Article200, related_name='ArtNoLnk400', on_delete=models.CASCADE, blank=True,
                                  null=True)  # ArtNo 400
    gen_art_no = models.BigIntegerField(verbose_name="GenArtNo", blank=True, null=True)  # GenArtNo 400
    lnk_target_type = models.BigIntegerField(verbose_name="LnkTargetType", blank=True, null=True)  # LnkTargetType 400
    lnk_target_no = models.BigIntegerField(verbose_name="LnkTargetNo", blank=True, null=True)  # LnkTargetNo 400
    seq_no = models.BigIntegerField(verbose_name="SeqNo", blank=True, null=True)  # SeqNo 400

    def __str__(self):
        return self.art_no_id.art_no


class Table404(models.Model):
    art_no_id = models.ForeignKey(Article200, related_name='ArtNoTable404', on_delete=models.CASCADE, blank=True,
                                  null=True)  # ArtNo 404
    gen_art_no = models.BigIntegerField(verbose_name="GenArtNo", blank=True, null=True)  # GenArtNo 404
    lnk_target_type = models.BigIntegerField(verbose_name="LnkTargetType", blank=True, null=True)  # LnkTargetType 404
    lnk_target_no = models.BigIntegerField(verbose_name="LnkTargetNo", blank=True, null=True)  # LnkTargetNo 404
    sort_no = models.BigIntegerField(verbose_name="sort_no", blank=True, null=True)  # sort_no 404

    def __str__(self):
        return self.art_no_id.art_no


class Table410(models.Model):
    art_no_id = models.ForeignKey(Article200, related_name='ArtNoTable410', on_delete=models.CASCADE, blank=True,
                                  null=True)  # ArtNo 410
    gen_art_no = models.BigIntegerField(verbose_name="GenArtNo", blank=True, null=True)  # GenArtNo 410
    lnk_target_type = models.BigIntegerField(verbose_name="LnkTargetType", blank=True, null=True)  # LnkTargetType 410
    lnk_target_no = models.BigIntegerField(verbose_name="LnkTargetNo", blank=True, null=True)  # LnkTargetNo 410
    seq_no = models.BigIntegerField(verbose_name="SeqNo", blank=True, null=True)  # SeqNo 410
    crit_no = models.CharField(max_length=255, verbose_name="CritNo", blank=True, null=True)  # CritNo 410
    crit_val = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)  # CritVal 410
    first_page = models.BigIntegerField(verbose_name="FirstPage", blank=True, null=True)  # FirstPage 410
    sort_no = models.BigIntegerField(verbose_name="sort_no", blank=True, null=True)  # sort_no 410

    def __str__(self):
        return self.art_no_id.art_no
