from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Hello About")


def contact(request):
    return HttpResponse(f"{request.path}")

def data(request,id):
    return HttpResponse(f"{id}")
 
#using query string
def team(request):
    if request.GET and 'm_id' in request.GET and 'c_id' in request.GET:
        return HttpResponse(f"hello member {request.GET.get('m_id')} you are {request.GET.get('c_id')}")
    else:
        return HttpResponse("Kuch to saram kar ")
