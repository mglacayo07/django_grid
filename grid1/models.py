from django.db import models
from .djgrid import JqGrid
from django.urls import reverse_lazy


class MyModel(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=100)
    url = models.URLField()
    height = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class ExampleGrid(JqGrid):
    model = MyModel  # could also be a queryset
    fields = ['id', 'name', 'desc', 'url', 'height']  # optional
    url = reverse_lazy('grid1:grid_handler')
    # caption = 'My First Grid'  # optional
    colmodel_overrides = {  # optional
        'id': {'editable': False, 'width': 10},
    }
    extra_config = {
        'multiselect': True,
        'multiboxonly': True,
        'toolbar': [True, 'up'],
        'rownumbers': True,
        'shrinkToFit': True,
        'height':'300px',
        'pager':'jqGrid_pager'
    }