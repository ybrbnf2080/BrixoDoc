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


admin.site.site_header = "BrixoDoc"
admin.site.register(Suppliers200)
admin.site.register(Article200)
admin.site.register(Country202)
admin.site.register(Manufacture203)
admin.site.register(Ref203)
admin.site.register(Supers204)
admin.site.register(CritVal210, CritValAdmin)
admin.site.register(Crit210, CritAdmin)
admin.site.register(Trade207)
admin.site.register(Doc231and232)
admin.site.register(Lnk400)
admin.site.register(Table404)
admin.site.register(Table410)