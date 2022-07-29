from django.db import models


class VehicleBrands(models.Model):
    Name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)

    class Meta:
        default_related_name = 'VehicleBrands'

    def __str__(self):
        return self.Name


class VehicleModels(models.Model):
    VehicleBrandId = models.ForeignKey(VehicleBrands, on_delete=models.CASCADE, related_name='VehicleModels',
                                       blank=True, null=True)
    Name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)
    ModelNumber = models.IntegerField(verbose_name="ModelNumber", blank=True, null=True)

    class Meta:
        default_related_name = 'VehicleModels'

    def __str__(self):
        return self.Name


class Vehicles(models.Model):
    VehicleModelId = models.ForeignKey(VehicleModels, on_delete=models.CASCADE, related_name='Vehicles', blank=True,
                                       null=True)
    TypeNumber = models.IntegerField(verbose_name="TypeNumber", blank=True, null=True)
    Year = models.CharField(max_length=255, verbose_name="Year", blank=True, null=True)
    BodyType = models.CharField(max_length=255, verbose_name="BodyType", blank=True, null=True)
    DriveType = models.CharField(max_length=255, verbose_name="DriveType", blank=True, null=True)
    EngineType = models.CharField(max_length=255, verbose_name="EngineType", blank=True, null=True)
    ValvesPerChamber = models.IntegerField(verbose_name="ValvesPerChamber", blank=True, null=True)
    Cylinders = models.IntegerField(verbose_name="Cylinders", blank=True, null=True)
    Volume = models.IntegerField(verbose_name="Volume", blank=True, null=True)
    CcmTech = models.IntegerField(verbose_name="CcmTech", blank=True, null=True)
    FuelType = models.CharField(max_length=255, verbose_name="FuelType", blank=True, null=True)
    FuelMixtureFormation = models.CharField(max_length=255, verbose_name="FuelMixtureFormation", blank=True, null=True)
    HorsePowers = models.CharField(max_length=255, verbose_name="HorsePowers", blank=True, null=True)
    KiloWatts = models.CharField(max_length=255, verbose_name="KiloWatts", blank=True, null=True)
    Engines = models.CharField(max_length=255, verbose_name="Engines", blank=True, null=True)
    TypeName = models.CharField(max_length=255, verbose_name="TypeName", blank=True, null=True)

    def __str__(self):
        return self.TypeName


class Suppliers(models.Model):
    Name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)

    def __str__(self):
        return self.Name


class Articles(models.Model):
    ExternalId = models.CharField(max_length=255, verbose_name="ExternalId", blank=True, null=True)
    SupplierId = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='Articles', blank=True, null=True)
    AssemblyGroup = models.CharField(max_length=255, verbose_name="AssemblyGroup", blank=True, null=True)
    GenericArticle = models.CharField(max_length=255, verbose_name="GenericArticle", blank=True, null=True)
    ArticleNumber = models.CharField(max_length=255, verbose_name="ArticleNumber", blank=True, null=True)
    Type = models.IntegerField(verbose_name="Type", blank=True, null=True)
    GenericArticleNumber = models.CharField(max_length=255, verbose_name="GenericArticleNumber", blank=True, null=True)
    Attributes = models.JSONField(verbose_name='Attributes', blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    Gtin = models.CharField(max_length=255, verbose_name="Gtin", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    StatusDat = models.IntegerField(verbose_name="StatusDat", blank=True, null=True)

    def __str__(self):
        return self.ArticleNumber


class Country(models.Model):
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Articles', blank=True, null=True)
    CountryCode = models.CharField(max_length=255, verbose_name="CountryCode", blank=True, null=True)

    def __str__(self):
        return self.CountryCode


class Supers(models.Model):
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Article', blank=True, null=True)
    SupersNo = models.CharField(max_length=255, verbose_name="CountryCode", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.SupersNo


class Trade(models.Model):
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Articl', blank=True, null=True)
    TradeNo = models.CharField(max_length=255, verbose_name="TradeNo", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.TradeNo


class Crit(models.Model):
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Artic', blank=True, null=True)
    CritNo = models.IntegerField(verbose_name="CritNo", blank=True, null=True)
    CritVal = models.CharField(max_length=255, verbose_name="CritVal", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)

    def __str__(self):
        return self.CritNo


class Doc(models.Model):
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Arti', blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    LangNo = models.IntegerField( verbose_name="LangNo", blank=True, null=True)
    DocName = models.CharField(max_length=255, verbose_name="DocName", blank=True, null=True)
    DocContentType = models.IntegerField(verbose_name="DocContentType", blank=True, null=True)
    DocTermNorm = models.IntegerField(verbose_name="DocTermNorm", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)

    def __str__(self):
        return self.DocName


class LnkTarget(models.Model):
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Art', blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)

    def __str__(self):
        return self.LnkTargetNo


class File(models.Model):
    Path = models.CharField(max_length=255, verbose_name="Path", blank=True, null=True)
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='File', blank=True, null=True)
    VehicleId = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='File', blank=True, null=True)
    Order = models.CharField(max_length=255, verbose_name="Order", blank=True, null=True)

    def __str__(self):
        return self.Path


class ArticlesToVehicle(models.Model):
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='ArticlesToVehicle', blank=True,
                                  null=True)
    VehicleId = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='ArticlesToVehicle', blank=True,
                                  null=True)
    Criterias = models.CharField(max_length=255, verbose_name="Criterias", blank=True, null=True)
    ExternalId = models.CharField(max_length=255, verbose_name="ExternalId", blank=True, null=True)

    def __str__(self):
        return self.ExternalId


class ArticleOem(models.Model):
    Brand = models.CharField(max_length=255, verbose_name="Brand", blank=True, null=True)
    OemNumber = models.CharField(max_length=255, verbose_name="OemNumber", blank=True, null=True)
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='ArticleOem', blank=True, null=True)
    IsOriginal = models.IntegerField(verbose_name="IsOriginal", blank=True, null=True)
    NormalizerOemNumber = models.CharField(max_length=255, verbose_name="NormalizerOemNumber", blank=True, null=True)
    IsReplacer = models.IntegerField(verbose_name="IsReplacer", blank=True, null=True)
    ManNo = models.IntegerField(verbose_name="ManNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)

    def __str__(self):
        return self.Brand


class Marketplaces(models.Model):
    Type = models.IntegerField(verbose_name="Type", blank=True, null=True)
    OzonId = models.IntegerField(verbose_name="OzonId", blank=True, null=True)
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Marketplaces', blank=True,
                                  null=True)

    def __str__(self):
        return self.ArticleId


class DisplayBra(models.Model):
    bra_brand_no = models.CharField(max_length=255, verbose_name="bra_brand_no", blank=True, null=True)
    bra_short_name = models.CharField(max_length=255, verbose_name="bra_short_name", blank=True, null=True)
    view_term_plain = models.CharField(max_length=255, verbose_name="view_term_plain", blank=True, null=True)

    def __str__(self):
        return self.bra_short_name