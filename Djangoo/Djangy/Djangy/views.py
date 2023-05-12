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

def login(request):
    punctuation= '''~`#,^*-{]'"/\?'''
    hidden_text=request.GET.get('text', 'default')
    value=''
    for char in hidden_text:
        if char not in punctuation:
            value = value + char
    params = {'key':value}
    return render(request, 'analyze.html', params)