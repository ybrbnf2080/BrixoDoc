from django.db import models


class Supliers_200(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)
    brand_no = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)

    def __str__(self):
        return self.name


class Country_202(models.Model):
    country_code = models.CharField(max_length=255, verbose_name="CountryCode", blank=True, null=True)
    country_name = models.CharField(max_length=255, verbose_name="CountryName", blank=True, null=True)

    def __str__(self):
        return self.country_code


class Manufacture_203(models.Model):
    ManNo = models.IntegerField(verbose_name="ManNo", blank=True, null=True)
    ShortName = models.CharField(max_length=255, verbose_name="ShortName", blank=True, null=True)
    TermPlain = models.CharField(max_length=255, verbose_name="TermPlain", blank=True, null=True)

    def __str__(self):
        return self.ShortName


class Ref_203(models.Model):
    RefNo = models.CharField(max_length=255, verbose_name="RefNo", blank=True, null=True)
    ManNoId = models.ForeignKey(Manufacture_203, on_delete=models.CASCADE, related_name='ManNoRef_203', blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.RefNo


class Supers_204(models.Model):
    SupersNo = models.CharField(max_length=255, verbose_name="SupersNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.SupersNo


class Article_200(models.Model):
    country = models.ManyToManyField(Country_202, blank=True, related_name='CountryArticle_200')
    gen_art_no = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    brand_no_id = models.ForeignKey(Supliers_200, on_delete=models.CASCADE, related_name='brand_no_article', blank=True, null=True)
    gtin = models.IntegerField(verbose_name="GTIN", blank=True, null=True)
    art_no = models.CharField(max_length=255, verbose_name="ArtNo", blank=True, null=True)
    quant_unit = models.IntegerField(verbose_name="QuantUnit", blank=True, null=True)
    quant_per_unit = models.IntegerField(verbose_name="QuantPerUnit", blank=True, null=True)
    art_stat = models.IntegerField(verbose_name="ArtStat", blank=True, null=True)
    status_dat = models.IntegerField(verbose_name="StatusDat", blank=True, null=True)
    ref_no_id = models.ManyToManyField(Ref_203, blank=True, related_name='ref_no_article')
    supers_id = models.ManyToManyField(Supers_204, blank=True, null=True, related_name='supers_article')

    def __str__(self):
        return self.art_no


class CritName_210(models.Model):
    CritNo = models.CharField(max_length=255, verbose_name="CrtNo", blank=True, null=True)
    CritName = models.CharField(max_length=255, verbose_name="CrtName", blank=True, null=True)
    Description = models.TextField(verbose_name="Description", blank=True, null=True)

    def __str__(self):
        return self.CritNo


class Crit_210(models.Model):
    ArtNoId = models.ForeignKey(Article_200, on_delete=models.CASCADE, related_name='ArtNoCrit_210', blank=True, null=True)
    CritNoId = models.ForeignKey(CritName_210, on_delete=models.CASCADE, related_name='CritNoCrit_210', blank=True, null=True)
    CritVal = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.CritVal


class Trade_207(models.Model):
    TradeNo = models.CharField(max_length=255, verbose_name="TradeNo", blank=True, null=True)
    ArtNoId = models.ForeignKey(Article_200, on_delete=models.CASCADE, related_name='ArtNoTrade_207', blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.TradeNo


class Doc_231_232(models.Model):
    ArtNoId = models.ForeignKey(Article_200, on_delete=models.CASCADE, related_name='ArtNoDoc_231_232', blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    LangNo = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    DocName = models.CharField(max_length=255, verbose_name="DocName", blank=True, null=True)
    DocContentType = models.IntegerField(verbose_name="DocContentType", blank=True, null=True)
    DocTermNorm = models.IntegerField(verbose_name="DocTermNorm", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)

    def __str__(self):
        return self.DocName


class Lnk(models.Model):
    ArtNo = models.ForeignKey(Article_200, on_delete=models.CASCADE, related_name='ArtNoLnk', blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)

    def __str__(self):
        return self.LnkTargetNo


class Table_404(models.Model):
    ArtNoId = models.ForeignKey(Article_200, on_delete=models.CASCADE, related_name='ArtNoTable_404', blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.LnkTargetNo


class Table_410(models.Model):
    ArtNoId = models.ForeignKey(Article_200, on_delete=models.CASCADE, related_name='ArtNoTable_410', blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    CritNo = models.CharField(max_length=255, verbose_name="CritNo", blank=True, null=True)
    CritVal = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)

    def __str__(self):
        return self.LnkTargetNo
