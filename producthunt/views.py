from django.http import HttpResponse 
from django.shortcuts import render 
import operator
from . import services
from django.views import generic
import requests
import json
from django.template import Library, Node,NodeList,Variable
import csv
import xml.etree.ElementTree as ET 
from django import template
import json as simplejson

register = template.Library()

def home(request):
    return render(request,'home.html')

def home(request):
    return render(request,'base.html')    



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
    harsh=hs['total_cases']
    
    x=[]
    for i in str(harsh):
        
        x.append(i)

    f=x[0]
    s=x[1]
    t=x[2]
    four=x[3]
    five=x[4]
    six=x[5]
    seventh=x[6]
        
    return render(request, 'corona/corona.html', {'user': hs,
    'first':f,
    'second':s,
    'third':t,
    'four':four,'five':five,'six':six,'seven':seventh})    


def search(request):
   
     return render(request,'search.html')

  


def coronas(request):
  
      


    
    
    harsh={'tamil nadu':'TN','tamilnadu':'TN','uttar pradesh':'UP','delhi':'DL','punjab':'PB','haryana':'HR','bihar':'BR','maharashtra':'MH','gujrat':'GJ','rajasthan':'RJ','telangana':'TG','kerala':'KL','assam':'AS','andhra pradesh':'AP','arunachal pradesh':'AR','chhattisgarh':'CT','goa':'GA','himachal pradesh':'HP',
    'jharkhand':'JH','karnataka':'KA','madhya pradesh':'MP','manipur':'MN','mizoram':'MZ','nagaland':'NL','odisha':'OR','sikkim':'SK',
    'uttarakhand':'UT','west bengal':'WB','andaman':'AN','orissa':'OR','jammu':'JK','jammu and kashmir':'JK',
    'puducherry':'PY','lakshadweep':'LD','ladakh':'LA','chandigarh':'CH','uttarpradesh':'UP'
    
    }
    full=request.GET.get('fulltext',None)
    full=full.lower()
    if full:
      
        if full in harsh:
            empty={}
            url = ("https://covid19india.p.rapidapi.com/getStateData/"+harsh[full])

            querystring = {"region":"TN"}


            headers = {
                'x-rapidapi-host': "covid19india.p.rapidapi.com",
                'x-rapidapi-key': "f4b5d5f55dmsh1f316c325f37d65p1365c9jsn64bb22164d1f"
                }

            response = requests.request("GET", url, headers=headers,params=querystring)
            empty=response.json()
            return render(request,'corona.html',{'empty':empty})
        else:
            return render(request,'home.html')
    
    else:
        return render(request,'home.html')
    



@register.filter(name='zip')
def country(request):
    country={}
    url='https://api.covid19india.org/v2/state_district_wise.json'
    response=requests.get(url)
    country=response.json()
    x=[]
    for i in range(len(country)):
        x+=(country[i]['districtData'])
        y=x
    y
    mylist = zip(country,y)
    
    z=[]    
    
    for i in range(len(country)):
        
        state2={country[i]['state']:country[i]['districtData']}
        z.append(state2)   
        n=z
    n
    return render(request,'country.html',{'country':country,'n':n,'y':y,'mylist':mylist})


def location(request):
    url = "http://ip-api.com/json"
    headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }
    response = requests.request("GET", url)
    locate=response.json()
   
    country={}
    urls='https://api.covid19india.org/v2/state_district_wise.json'
    responses=requests.get(urls)
    country=responses.json()
   

    x=[]
    for i in range(len(country)):
        x+=(country[i]['districtData'])
        y=x
    y
    z=[]
    for j in range(len(y)):
        z=y[j]['district']
          
    z
    res = [ sub['district'] for sub in y ]
    rest=set(res)
    json_list=simplejson.dumps(res)
    dist=[]
    do=[",".join(res)]
    dos=do[0]
    
    return render(request,'location.html',{'locate':locate,'x':dos,'jsons':json_list})
