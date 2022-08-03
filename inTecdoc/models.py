from django.db import models


class Suppliers200(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)
    brand_no = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)

    def __str__(self):
        return self.name


class Country202(models.Model):
    country_code = models.CharField(max_length=255, verbose_name="CountryCode", blank=True, null=True)
    country_name = models.CharField(max_length=255, verbose_name="CountryName", blank=True, null=True)

    def __str__(self):
        return self.country_code


class Manufacture203(models.Model):
    man_no = models.IntegerField(verbose_name="ManNo", blank=True, null=True)
    short_name = models.CharField(max_length=255, verbose_name="ShortName", blank=True, null=True)
    term_plain = models.CharField(max_length=255, verbose_name="TermPlain", blank=True, null=True)

    def __str__(self):
        return self.short_name


class Ref203(models.Model):
    ref_no = models.CharField(max_length=255, verbose_name="RefNo", blank=True, null=True)
    man_no_id = models.ForeignKey(Manufacture203, on_delete=models.CASCADE, verbose_name='ManNoName', blank=True, null=True)

    def __str__(self):
        return self.ref_no


class Supers204(models.Model):
    supers_no = models.CharField(max_length=255, verbose_name="SupersNo", blank=True, null=True)
    sort_no = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.supers_no


class Article200(models.Model):
    country = models.ManyToManyField(Country202, blank=True, related_name='CountryArticle_200')
    gen_art_no = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    brand_no_id = models.ForeignKey(Suppliers200, on_delete=models.CASCADE, related_name='brand_no_article', blank=True,
                                    null=True)
    gtin = models.IntegerField(verbose_name="GTIN", blank=True, null=True)
    art_no = models.CharField(max_length=255, verbose_name="ArtNo", blank=True, null=True)
    quant_unit = models.IntegerField(verbose_name="QuantUnit", blank=True, null=True)
    quant_per_unit = models.IntegerField(verbose_name="QuantPerUnit", blank=True, null=True)
    art_stat = models.IntegerField(verbose_name="ArtStat", blank=True, null=True)
    status_dat = models.IntegerField(verbose_name="StatusDat", blank=True, null=True)
    ref_no_id = models.ManyToManyField(Ref203, blank=True, related_name='ref_no_article')
    supers_id = models.ManyToManyField(Supers204, blank=True, related_name='supers_article')

    def __str__(self):
        return self.art_no


class CritVal210(models.Model):
    crit_no = models.IntegerField(verbose_name="CritNo", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)

    def __str__(self):
        return self.name


class Crit210(models.Model):
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, verbose_name="ArtNo", blank=True, null=True)
    crit_no_id = models.ForeignKey(CritVal210, on_delete=models.CASCADE, verbose_name="CritNo", blank=True, null=True)
    crit_val = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)

    def __str__(self):
        return self.crit_val


class Trade207(models.Model):
    trade_no = models.CharField(max_length=255, verbose_name="TradeNo", blank=True, null=True)
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, related_name='ArtNoTrade_207', blank=True,
                                  null=True)
    first_page = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    sort_no = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.trade_no


class Doc231and232(models.Model):
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, related_name='ArtNoDoc_231_232', blank=True,
                                  null=True)
    doc_no = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    lang_no = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    doc_name = models.CharField(max_length=255, verbose_name="DocName", blank=True, null=True)
    doc_content_type = models.IntegerField(verbose_name="DocContentType", blank=True, null=True)
    doc_term_no = models.IntegerField(verbose_name="DocTermNorm", blank=True, null=True)
    doc_type = models.IntegerField(verbose_name="DocType", blank=True, null=True)

    def __str__(self):
        return self.doc_name


class Lnk400(models.Model):
    art_no = models.ForeignKey(Article200, on_delete=models.CASCADE, related_name='ArtNoLnk', blank=True, null=True)
    lnk_target_no = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    lnk_target_type = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    seq_no = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)

    def __str__(self):
        return self.lnk_target_no


class Table404(models.Model):
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, related_name='ArtNoTable_404', blank=True,
                                  null=True)
    lnk_target_type = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    lnk_target_no = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    sort_no = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.lnk_target_no


class Table410(models.Model):
    art_no_id = models.ForeignKey(Article200, on_delete=models.CASCADE, related_name='ArtNoTable_410', blank=True,
                                  null=True)
    lnk_target_type = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    lnk_target_no = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    seq_no = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    sort_no = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    crit_no = models.CharField(max_length=255, verbose_name="CritNo", blank=True, null=True)
    crit_val = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)
    first_page = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)

    def __str__(self):
        return self.lnk_target_no
