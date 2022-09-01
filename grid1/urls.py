from django.urls import path, include, re_path
from .views import GridView, GridView2, GridView3, grid_config, grid_handler

grid1_patterns = (
    [
        # Basic Grid
        path('', GridView.as_view(), name="json"),
        # Data Base Grid
        path('2/', GridView2.as_view(), name="database"),
        path('3/', GridView3.as_view(), name="mixin"),
        path('examplegrid/', grid_handler, name='grid_handler'),
        path('examplegrid/cfg/', grid_config, name='grid_config'),
    ], 'grid1')
