from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("This is django program!")
def index(request):
    template = loader.get_template('sample.html')
    return HttpResponse(template.render())
    


