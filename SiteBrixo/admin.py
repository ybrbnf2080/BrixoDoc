from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class ArticleAdmin(ModelAdmin):
    list_display = ['id',
                    'ExternalId',
                    'SupplierId',
                    'AssemblyGroup',
                    'GenericArticle',
                    'ArticleNumber',
                    'Type',
                    'GenericArticleNumber',
                    ]
    search_fields = ['ArticleNumber', 'ExternalId']


class CountryAdmin(ModelAdmin):
    list_display = ['id',
                    'Article',
                    'CountryCode'
                    ]
    search_fields = ['Article', 'CountryCode']


class OemAdmin(ModelAdmin):
    list_display = ['id',
                    'Brand',
                    'OemNumber',
                    'ArticleId',
                    'IsOriginal',
                    'NormalizerOemNumber',
                    'IsReplacer'
                    ]
    search_fields = ['OemNumber', 'Brand']


class VehicleModelAdmin(ModelAdmin):
    list_display = ['id',
                    'VehicleBrandId',
                    'Name',
                    'ModelNumber'
                    ]
    search_fields = ['Name']


class VehicleBrandAdmin(ModelAdmin):
    list_display = ['id',
                    'Name',
                    ]
    search_fields = ['Name']


class VehiclesAdmin(ModelAdmin):
    list_display = ['id',
                    'VehicleModelId',
                    'TypeNumber',
                    'Year',
                    'BodyType',
                    'DriveType',
                    'EngineType',
                    'ValvesPerChamber',
                    'Cylinders',
                    'Volume',
                    'CcmTech',
                    'FuelType',
                    'FuelMixtureFormation',
                    'HorsePowers',
                    'KiloWatts',
                    'Engines',
                    'TypeName',
                    ]


class VehicleToArticleAdmin(ModelAdmin):
    list_display = ['id',
                    'ArticleId',
                    'VehicleId',
                    'Criterias',
                    'ExternalId',
                    ]
    search_fields = ['ExternalId']


class DisplayBraAdmin(ModelAdmin):
    list_display = ['id',
                    'bra_brand_no',
                    'bra_short_name',
                    'view_term_plain',
                    ]
    search_fields = ['bra_brand_no', 'bra_short_name', 'view_term_plain',]


class SuppliersAdmin(ModelAdmin):
    list_display = ['id',
                    'Name',
                    'BrandNo',
                    ]
    search_fields = ['Name', 'BrandNo']


admin.site.register(VehicleBrands, VehicleBrandAdmin)
admin.site.register(VehicleModels, VehicleModelAdmin)
admin.site.register(Vehicles, VehiclesAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(Articles, ArticleAdmin)
admin.site.register(File)
admin.site.register(ArticlesToVehicle, VehicleToArticleAdmin)
admin.site.register(ArticleOem, OemAdmin)
admin.site.register(Marketplaces)
admin.site.register(DisplayBra, DisplayBraAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Supers)
admin.site.register(Trade)
admin.site.register(Crit)
admin.site.register(Doc)
admin.site.register(LnkTarget)
