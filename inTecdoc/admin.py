from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class CritAdmin(ModelAdmin):
    list_display = ['id',
                    'art_no_id',
                    'crit_no_id',
                    'crit_val'
                    ]


class CritValAdmin(ModelAdmin):
    list_display = ['id',
                    'crit_no',
                    'name'
                    ]


class SuppliersAdmin(ModelAdmin):
    list_display = ['id',
                    'brand_no',
                    'name'
                    ]


class DocAdmin(ModelAdmin):
    list_display = ['id',
                    'doc_no',
                    'doc_name'
                    ]
    search_fields = ['doc_name']


class CountryInline(admin.TabularInline):
    model = Article200.country_id.through


class DocInline(admin.TabularInline):
    model = Article200.doc_no_id.through


class ArticleAdmin(ModelAdmin):
    list_display = ['id',
                    'art_no',
                    'gen_art_no',
                    'brand_no_id'
                    ]
    search_fields = ['art_no']
    # filter_horizontal = ('doc_no_id', 'country_id')
    inlines = [
        CountryInline,
        DocInline,
    ]
    exclude = ('doc_no_id', 'country_id')


class ManufactureAdmin(ModelAdmin):
    list_display = ['id',
                    'man_no',
                    'short_name',
                    'term_plain'
                    ]


class RefAdmin(ModelAdmin):
    list_display = ['id',
                    'art_no_id',
                    'ref_no',
                    'man_no_id'
                    ]
    search_fields = ['ref_no']


class Trade207Admin(ModelAdmin):
    list_display = ['id',
                    'art_no_id',
                    'trade_no'
                    ]
    search_fields = ['trade_no']


class SupersAdmin(ModelAdmin):
    list_display = ['id',
                    'art_no_id',
                    'supers_no'
                    ]
    search_fields = ['supers_no']


class Lnk400Admin(ModelAdmin):
    list_display = ['id',
                    'art_no_id',
                    'gen_art_no',
                    'lnk_target_type',
                    'lnk_target_no',
                    'seq_no',
                    ]
    search_fields = ['lnk_target_no']


class VehicleAdmin(ModelAdmin):
    list_display = ['id',
                    'veh_type_no',
                    'veh_model_no',
                    'veh_brand',
                    'veh_type_name',
                    'engine_code',
                    'ccm_tech',
                    ]
    search_fields = ['veh_type_no']

admin.site.site_header = "BrixoDoc"
admin.site.register(Suppliers200, SuppliersAdmin)
admin.site.register(Article200, ArticleAdmin)
admin.site.register(Country202)
admin.site.register(Manufacture203, ManufactureAdmin)
admin.site.register(Ref203, RefAdmin)
admin.site.register(Supers204, SupersAdmin)
admin.site.register(CritVal210, CritValAdmin)
admin.site.register(Crit210, CritAdmin)
admin.site.register(Trade207, Trade207Admin)
admin.site.register(Doc231and232, DocAdmin)
admin.site.register(Lnk400, Lnk400Admin)
admin.site.register(Table404)
admin.site.register(Table410)
admin.site.register(Vehicles, VehicleAdmin)