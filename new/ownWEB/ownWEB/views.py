from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hellllo")
    return render(request, "index.html" )
    

def contact(request):
    request.Get.get('text', 'default')
    return render(request,"dev.html")

def about(request):
    return render(request, "prac.html")

def search(request):
    return HttpResponse("<button><a href='/about'>back</a></button>")