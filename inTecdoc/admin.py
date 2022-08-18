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


class ArticleAdmin(ModelAdmin):
    list_display = ['id',
                    'art_no',
                    'gen_art_no',
                    'brand_no_id'
                    ]
    search_fields = ['art_no']


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


class Lnk400Admin(ModelAdmin):
    list_display = ['id',
                    'art_no_id',
                    'gen_art_no',
                    'lnk_target_type',
                    'lnk_target_no',
                    'seq_no',
                    ]
    search_fields = ['lnk_target_no']

admin.site.site_header = "BrixoDoc"
admin.site.register(Suppliers200, SuppliersAdmin)
admin.site.register(Article200, ArticleAdmin)
admin.site.register(Country202)
admin.site.register(Manufacture203, ManufactureAdmin)
admin.site.register(Ref203, RefAdmin)
admin.site.register(Supers204)
admin.site.register(CritVal210, CritValAdmin)
admin.site.register(Crit210, CritAdmin)
admin.site.register(Trade207, Trade207Admin)
admin.site.register(Doc231and232, DocAdmin)
admin.site.register(Lnk400, Lnk400Admin)
admin.site.register(Table404)
admin.site.register(Table410)