from django.contrib import admin
from .models import *


class TankAdmin(admin.ModelAdmin):
    list_display = ['title', 'strana', 'klas', 'publish']
    list_editable = ['publish']
    list_filter = ['strana', 'klas', 'publish']


class StranaAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish']


class KlasAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish']


admin.site.register(Tank, TankAdmin)
admin.site.register(Strana, StranaAdmin)
admin.site.register(Klas, KlasAdmin)

