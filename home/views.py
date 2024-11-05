from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    hom = home_model.objects.all()
    con = {
        'hom': hom  # Change this to 'hom' to match the template
    }
    return render(request, template_name='home/index.html', context=con)

def looking_for(request):
    return render(request, template_name='home/looking_for.html', )

def appertment(request):
    return render(request, template_name='home/appertment.html', )