from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse
from .models import ExampleGrid, MyModel


# Basic Grid
class GridView(TemplateView):
    template_name = "grid1/grid.html"

    def get(self, request, *args, **kwargs):
        kw = {
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)


# Data Base Grid
def grid_handler(request):
    # handles pagination, sorting and searching
    grid = ExampleGrid()
    print(grid.get_json(request))
    return HttpResponse(grid.get_json(request), content_type="application/json")


def grid_config(request):
    # build a config suitable to pass to jqgrid constructor
    grid = ExampleGrid()
    print(grid.get_config())
    return HttpResponse(grid.get_config(), content_type="application/json")


class GridView2(TemplateView):
    template_name = "grid1/grid2.html"

    def get(self, request, *args, **kwargs):
        kw = {
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)


class GridView3(TemplateView):
    template_name = "grid1/grid3.html"

    def get(self, request, *args, **kwargs):
        kw = {
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)