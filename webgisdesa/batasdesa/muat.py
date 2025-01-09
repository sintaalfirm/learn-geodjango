import os
from django.contrib.gis.utils import LayerMapping
from .models import BangunanPogung # definisi gismodel dari 'modelspy'

bangunanpogung_mapping = {
    'nama': 'Nama',
    'jenis': 'Jenis',
    'pemilik': 'Pemilik',
    'geom': 'MULTIPOLYGON',
}

bangunanpogung_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'bangunan_pogung.shp'),
)

def run(verbose=True):
    lm = LayerMapping(BangunanPogung, bangunanpogung_shp, bangunanpogung_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)