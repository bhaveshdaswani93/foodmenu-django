from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }

    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse('<h1>This is an Item view.</h1>')
