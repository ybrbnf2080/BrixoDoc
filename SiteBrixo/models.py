from django.db import models


class VehicleBrands(models.Model):
    Name = models.TextField(verbose_name="Name", blank=True, null=True)

    def __str__(self):
        return self.Name


class VehicleModels(models.Model):
    VehicleBrandId = models.ForeignKey(VehicleBrands, on_delete=models.CASCADE, related_name='VehicleModels',
                                       blank=True, null=True)
    Name = models.TextField(verbose_name="Name", blank=True, null=True)
    ModelNumber = models.IntegerField(verbose_name="ModelNumber", blank=True, null=True)

    def __str__(self):
        return self.Name


class Vehicles(models.Model):
    VehicleModelId = models.ForeignKey(VehicleModels, on_delete=models.CASCADE, related_name='Vehicles', blank=True,
                                       null=True)
    TypeNumber = models.IntegerField(verbose_name="TypeNumber", blank=True, null=True)
    Year = models.TextField(verbose_name="Year", blank=True, null=True)
    BodyType = models.TextField(verbose_name="BodyType", blank=True, null=True)
    DriveType = models.TextField(verbose_name="DriveType", blank=True, null=True)
    EngineType = models.TextField(verbose_name="EngineType", blank=True, null=True)
    ValvesPerChamber = models.IntegerField(verbose_name="ValvesPerChamber", blank=True, null=True)
    Cylinders = models.IntegerField(verbose_name="Cylinders", blank=True, null=True)
    Volume = models.IntegerField(verbose_name="Volume", blank=True, null=True)
    CcmTech = models.IntegerField(verbose_name="CcmTech", blank=True, null=True)
    FuelType = models.TextField(verbose_name="FuelType", blank=True, null=True)
    FuelMixtureFormation = models.TextField(verbose_name="FuelMixtureFormation", blank=True, null=True)
    HorsePowers = models.TextField(verbose_name="HorsePowers", blank=True, null=True)
    KiloWatts = models.TextField(verbose_name="KiloWatts", blank=True, null=True)
    Engines = models.TextField(verbose_name="Engines", blank=True, null=True)
    TypeName = models.TextField(verbose_name="TypeName", blank=True, null=True)

    def __str__(self):
        return self.TypeName


class Suppliers(models.Model):
    Name = models.TextField(verbose_name="Name", blank=True, null=True)

    def __str__(self):
        return self.Name


class Articles(models.Model):
    ExternalId = models.TextField(verbose_name="ExternalId", blank=True, null=True)
    SupplierId = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='Articles', blank=True, null=True)
    AssemblyGroup = models.TextField(verbose_name="AssemblyGroup", blank=True, null=True)
    GenericArticle = models.TextField(verbose_name="GenericArticle", blank=True, null=True)
    ArticleNumber = models.CharField(max_length=255, verbose_name="ArticleNumber", blank=True, null=True)
    Type = models.IntegerField(verbose_name="Type", blank=True, null=True)
    GenericArticleNumber = models.TextField(verbose_name="GenericArticleNumber", blank=True, null=True)
    Attributes = models.TextField(verbose_name='Attributes', blank=True, null=True)

    def __str__(self):
        return self.ArticleNumber


class File(models.Model):
    Path = models.TextField(verbose_name="Path", blank=True, null=True)
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='File', blank=True, null=True)
    VehicleId = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='File', blank=True, null=True)
    Order = models.TextField(verbose_name="Order", blank=True, null=True)

    def __str__(self):
        return self.Path


class ArticlesToVehicle(models.Model):
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='ArticlesToVehicle', blank=True,
                                  null=True)
    VehicleId = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='ArticlesToVehicle', blank=True,
                                  null=True)
    Criterias = models.TextField(verbose_name="Criterias", blank=True, null=True)
    ExternalId = models.TextField(verbose_name="ExternalId", blank=True, null=True)

    def __str__(self):
        return self.ExternalId


class ArticleOem(models.Model):
    Brand = models.TextField(verbose_name="Brand", blank=True, null=True)
    OemNumber = models.TextField(verbose_name="OemNumber", blank=True, null=True)
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='ArticleOem', blank=True, null=True)
    IsOriginal = models.IntegerField(verbose_name="IsOriginal", blank=True, null=True)
    NormalizerOemNumber = models.CharField(max_length=255, verbose_name="NormalizerOemNumber", blank=True, null=True)
    IsReplacer = models.IntegerField(verbose_name="IsReplacer", blank=True, null=True)

    def __str__(self):
        return self.Brand


class Marketplaces(models.Model):
    Type = models.IntegerField(verbose_name="Type", blank=True, null=True)
    OzonId = models.IntegerField(verbose_name="OzonId", blank=True, null=True)
    ArticleId = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='Marketplaces', blank=True,
                                  null=True)

    def __str__(self):
        return self.ArticleId
