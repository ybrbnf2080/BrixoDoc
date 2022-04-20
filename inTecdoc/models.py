from django.db import models


class Table001(models.Model):
    """
        Таблица №1
    """

    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    Data = models.IntegerField(verbose_name="Data", blank=True, null=True)
    Release = models.IntegerField(verbose_name="Release", blank=True, null=True)
    VersionDate = models.IntegerField(verbose_name="VersionDate", blank=True, null=True)
    Full = models.IntegerField(verbose_name="Full", blank=True, null=True)
    ManNo = models.IntegerField(verbose_name="ManNo", blank=True, null=True)
    BrandName = models.CharField(verbose_name="BrandName", max_length=255, blank=True, null=True)
    RefDataVersion = models.IntegerField(verbose_name="RefDataVersion", blank=True, null=True)
    Reserved = models.IntegerField(verbose_name="Reserved", blank=True, null=True)
    Format = models.CharField(verbose_name="Format", max_length=255, blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)



class Table030(models.Model):
    """
        Таблица №30
    """

    Reserved = models.CharField(verbose_name="Reserved", max_length=255, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    TermNo = models.IntegerField(verbose_name="TermNo", blank=True, null=True)
    LangNo = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    Term = models.CharField(verbose_name="Term", max_length=255, blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table035(models.Model):
    """
        Таблица №35
    """

    Reserved = models.CharField(verbose_name="Reserved", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    TxtModNo = models.CharField(verbose_name="TxtModNo", max_length=250, blank=True, null=True)
    LangNo = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    Fixed = models.IntegerField(verbose_name="Fixed", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    Text = models.CharField(verbose_name="", max_length=250, blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table040(models.Model):
    """
        Таблица №40
    """

    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    Term1 = models.CharField(verbose_name="Term1", max_length=250, blank=True, null=True)
    Term2 = models.CharField(verbose_name="Term2", max_length=250, blank=True, null=True)
    Street1 = models.CharField(verbose_name="Street1", max_length=250, blank=True, null=True)
    Street2 = models.CharField(verbose_name="Street2", max_length=250, blank=True, null=True)
    POBox = models.CharField(verbose_name="POBox", max_length=250, blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    PostCode = models.CharField(verbose_name="PostCode", max_length=250, blank=True, null=True)
    PostCodePOBox = models.CharField(verbose_name="PostCodePOBox", max_length=250, blank=True, null=True)
    PostCodeCus = models.CharField(verbose_name="PostCodeCus", max_length=250, blank=True, null=True)
    City1 = models.CharField(verbose_name="City1", max_length=250, blank=True, null=True)
    City2 = models.CharField(verbose_name="City2", max_length=250, blank=True, null=True)
    Phone = models.CharField(verbose_name="Phone", max_length=250, blank=True, null=True)
    Fax = models.CharField(verbose_name="Fax", max_length=250, blank=True, null=True)
    Email = models.CharField(verbose_name="Email", max_length=250, blank=True, null=True)
    Web = models.CharField(verbose_name="Web", max_length=250, blank=True, null=True)
    AdrType = models.IntegerField(verbose_name="AdrType", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table042(models.Model):
    """
    Таблица №42
    """

    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table043(models.Model):
    """
    Таблица №43
    """

    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    AdrType = models.IntegerField(verbose_name="AdrType", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    Term1 = models.CharField(verbose_name="Term1", max_length=250, blank=True, null=True)
    Term2 = models.CharField(verbose_name="Term2", max_length=250, blank=True, null=True)
    Street1 = models.CharField(verbose_name="Street1", max_length=250, blank=True, null=True)
    Street2 = models.CharField(verbose_name="Street2", max_length=250, blank=True, null=True)
    POBox = models.CharField(verbose_name="POBox", max_length=250, blank=True, null=True)
    CountryCode1 = models.CharField(verbose_name="CountryCode1", max_length=250, blank=True, null=True)
    PostCode = models.CharField(verbose_name="PostCode", max_length=250, blank=True, null=True)
    PostCodePOBox = models.CharField(verbose_name="PostCodePOBox", max_length=250, blank=True, null=True)
    PostCodeCus = models.CharField(verbose_name="PostCodeCus", max_length=250, blank=True, null=True)
    City1 = models.CharField(verbose_name="City1", max_length=250, blank=True, null=True)
    City2 = models.CharField(verbose_name="City2", max_length=250, blank=True, null=True)
    Phone = models.CharField(verbose_name="Phone", max_length=250, blank=True, null=True)
    Fax = models.CharField(verbose_name="Fax", max_length=250, blank=True, null=True)
    Email = models.CharField(verbose_name="Email", max_length=250, blank=True, null=True)
    Web = models.CharField(verbose_name="Web", max_length=250, blank=True, null=True)
    AdrType1 = models.IntegerField(verbose_name="AdrType1", blank=True, null=True)


class Table200(models.Model):
    """
    Таблица №200
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    TermNo = models.IntegerField(verbose_name="TermNo", blank=True, null=True)
    SelfServ = models.IntegerField(verbose_name="SelfServ", blank=True, null=True)
    MatCert = models.IntegerField(verbose_name="MatCert", blank=True, null=True)
    Remanufact = models.IntegerField(verbose_name="Remanufact", blank=True, null=True)
    Accessory = models.IntegerField(verbose_name="Accessory", blank=True, null=True)
    BatchSize1 = models.IntegerField(verbose_name="BatchSize1", blank=True, null=True)
    BatchSize2 = models.IntegerField(verbose_name="BatchSize2", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table201(models.Model):
    """
    Таблица №201
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    Price = models.IntegerField(verbose_name="Price", blank=True, null=True)
    PrUnit = models.IntegerField(verbose_name="PrUnit", blank=True, null=True)
    PrQuantUnit = models.CharField(verbose_name="PrQuantUnit", max_length=250, blank=True, null=True)
    ValidFrom = models.IntegerField(verbose_name="ValidFrom", blank=True, null=True)
    ValidTo = models.IntegerField(verbose_name="ValidTo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    PrType = models.IntegerField(verbose_name="PrType", blank=True, null=True)
    Reserved = models.CharField(verbose_name="Reserved", max_length=250, blank=True, null=True)
    CurCode = models.CharField(verbose_name="CurCode", max_length=250, blank=True, null=True)
    DiscGroup = models.CharField(verbose_name="DiscGroup", max_length=250, blank=True, null=True)
    Dicount = models.IntegerField(verbose_name="Dicount", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table202(models.Model):
    """
    Таблица №202
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table203(models.Model):
    """
    Таблица №203
    """

    ArtNO = models.CharField(verbose_name="ArtNO", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    ManNo = models.IntegerField(verbose_name="ManNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    RefNo = models.CharField(verbose_name="RefNo", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    Additive = models.IntegerField(verbose_name="Additive", blank=True, null=True)
    ReferenceInfo = models.CharField(verbose_name="ReferenceInfo", max_length=250, blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table204(models.Model):
    """
    Таблица №204
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    SupersNo = models.CharField(verbose_name="SupersNo", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table205(models.Model):
    """
    Таблица №205
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    PartGenArtNo = models.IntegerField(verbose_name="PartGenArtNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    PartNo = models.CharField(verbose_name="PartNo", max_length=250, blank=True, null=True)
    Quantity = models.IntegerField(verbose_name="Quantity", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table206(models.Model):
    """
    Таблица №206
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    Reserved = models.IntegerField(verbose_name="Reserved", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    InfType = models.IntegerField(verbose_name="InfType", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    TXTModNo = models.CharField(verbose_name="TXTModNo", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table207(models.Model):
    """
    Таблица №207
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    TradeNo = models.CharField(verbose_name="TradeNo", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table208(models.Model):
    """
    Таблица №208
    """

    ArtNo = models.IntegerField(verbose_name="ArtNo", blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TaleNo = models.IntegerField(verbose_name="TaleNo", blank=True, null=True)
    Reserved = models.IntegerField(verbose_name="Reserved", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    CritNo = models.IntegerField(verbose_name="CritNo", blank=True, null=True)
    CritVal = models.IntegerField(verbose_name="CritVal", blank=True, null=True)
    Reserved1 = models.IntegerField(verbose_name="Reserved1", blank=True, null=True)
    SeqNo1 = models.IntegerField(verbose_name="SeqNo1", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table209(models.Model):
    """
    Таблица №209
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    GTIN = models.IntegerField(verbose_name="GTIN", blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table210(models.Model):
    """
    Таблица №210
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    Reserved = models.IntegerField(verbose_name="Reserved", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    CritNo = models.IntegerField(verbose_name="CritNo", blank=True, null=True)
    CritVal = models.CharField(verbose_name="CritVal", max_length=250, blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table211(models.Model):
    """
    Таблица №211
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table212(models.Model):
    """
    Таблица №212
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    QuantUnit = models.CharField(verbose_name="QuantUnit", max_length=250, blank=True, null=True)
    QuantPerUnit = models.IntegerField(verbose_name="QuantPerUnit", blank=True, null=True)
    ArtStat = models.IntegerField(verbose_name="ArtStat", blank=True, null=True)
    StatusDat = models.IntegerField(verbose_name="StatusDat", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table215(models.Model):
    """
    Таблица №215
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table217(models.Model):
    """
    Таблица №217
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)
    LangNo = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    CoordNo = models.IntegerField(verbose_name="CoordNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table222(models.Model):
    """
    Таблица №222
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    LnkType = models.IntegerField(verbose_name="LnkType", blank=True, null=True)
    LnkVal = models.IntegerField(verbose_name="LnkVal", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    AccArtNo = models.CharField(verbose_name="AccArtNo", max_length=250, blank=True, null=True)
    Quantity = models.IntegerField(verbose_name="Quantity", blank=True, null=True)
    AccGenArtNo = models.IntegerField(verbose_name="AccGenArtNo", blank=True, null=True)
    Reserved = models.IntegerField(verbose_name="Reserved", blank=True, null=True)
    TermNo = models.IntegerField(verbose_name="TermNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table228(models.Model):
    """
    Таблица №228
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    SeqNo1 = models.IntegerField(verbose_name="SeqNo1", blank=True, null=True)
    SortNo1 = models.IntegerField(verbose_name="SortNo1", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    CritNo = models.IntegerField(verbose_name="CritNo", blank=True, null=True)
    CritVal = models.CharField(verbose_name="CritVal", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table231(models.Model):
    """
    Таблица №231
    """

    Reserved = models.CharField(verbose_name="Reserved", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    LangNo = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    DocName = models.CharField(verbose_name="DocName", max_length=250, blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)
    DocTermNorm = models.IntegerField(verbose_name="DocTermNorm", blank=True, null=True)
    Width = models.IntegerField(verbose_name="Width", blank=True, null=True)
    Height = models.IntegerField(verbose_name="Height", blank=True, null=True)
    Colors = models.IntegerField(verbose_name="Colors", blank=True, null=True)
    DocType1 = models.IntegerField(verbose_name="DocType1", blank=True, null=True)
    TermNo = models.CharField(verbose_name="TermNo", max_length=250, blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)
    URL = models.CharField(verbose_name="URL", max_length=250, blank=True, null=True)


class Table232(models.Model):
    """
    Таблица №232
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table233(models.Model):
    """
    Таблица №233
    """

    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)
    CoordNo = models.IntegerField(verbose_name="CoordNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    LangNo = models.IntegerField(verbose_name="LangNo", blank=True, null=True)
    Type = models.IntegerField(verbose_name="Type", blank=True, null=True)
    X1 = models.IntegerField(verbose_name="X1", blank=True, null=True)
    Y1 = models.IntegerField(verbose_name="Y1", blank=True, null=True)
    X2 = models.IntegerField(verbose_name="X2", blank=True, null=True)
    Y2 = models.IntegerField(verbose_name="Y2", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table400(models.Model):
    """
    Таблица №400
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table401(models.Model):
    """
    Таблица №401
    """

    ArtNr = models.CharField(verbose_name="ArtNr", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnktargetNo = models.IntegerField(verbose_name="LnktargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    InfType = models.IntegerField(verbose_name="InfType", blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    TxtModNo = models.CharField(verbose_name="TxtModNo", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table403(models.Model):
    """
    Таблица №403
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table404(models.Model):
    """
    Таблица №404
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table410(models.Model):
    """
    Таблица №410
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    CritNo = models.IntegerField(verbose_name="CritNo", blank=True, null=True)
    CritVal = models.CharField(verbose_name="CritVal", max_length=250, blank=True, null=True)
    FirstPage = models.IntegerField(verbose_name="FirstPage", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)


class Table432(models.Model):
    """
    Таблица №432
    """

    ArtNo = models.CharField(verbose_name="ArtNo", max_length=250, blank=True, null=True)
    BrandNo = models.IntegerField(verbose_name="BrandNo", blank=True, null=True)
    TableNo = models.IntegerField(verbose_name="TableNo", blank=True, null=True)
    GenArtNo = models.IntegerField(verbose_name="GenArtNo", blank=True, null=True)
    LnkTargetType = models.IntegerField(verbose_name="LnkTargetType", blank=True, null=True)
    LnkTargetNo = models.IntegerField(verbose_name="LnkTargetNo", blank=True, null=True)
    SeqNo = models.IntegerField(verbose_name="SeqNo", blank=True, null=True)
    CountryCode = models.CharField(verbose_name="CountryCode", max_length=250, blank=True, null=True)
    SortNo = models.IntegerField(verbose_name="SortNo", blank=True, null=True)
    DocNo = models.IntegerField(verbose_name="DocNo", blank=True, null=True)
    DocType = models.IntegerField(verbose_name="DocType", blank=True, null=True)
    Exclude = models.IntegerField(verbose_name="Exclude", blank=True, null=True)
    DeleteFlag = models.IntegerField(verbose_name="DeleteFlag", blank=True, null=True)
