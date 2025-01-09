from django.contrib import admin

# Register your models here.
from .models import BangunanPogung
from leaflet.admin import LeafletGeoAdmin

class AdminPogung(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (-7.760030, 110.376214), #atur zoom ke pogung
        'DEFAULT_ZOOM' : 14,
    }

# daftarkan model pada halaman admin
admin.site.register(BangunanPogung, AdminPogung)