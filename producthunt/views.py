from django.http import HttpResponse 
from django.shortcuts import render 
import operator
from . import services
from django.views import generic
import requests
import json


def home(request):
    return render(request,'home.html')



def base(request):
    return render(request,'base.html')


class BooksPage(generic.TemplateView):
    def get(self,request):
        books_list = services.get_totalcases('total_cases')
        return render(request,'home.html',books_list,{'total_cases':total_cases})

        
def corona(request):
    
    
    user = {}
    url = 'https://api.thevirustracker.com/free-api?global=stats'
    response = requests.get(url)
    user = response.json()
    h=user['results']
    hs=h[0]
    
        
    return render(request, 'corona.html', {'user': hs})    


def coronas(request):
    return render(request,'corona/coronas.html')    