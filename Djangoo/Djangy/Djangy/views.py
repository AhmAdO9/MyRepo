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
    punctuation= '''~`#,^*-{]'."/\?'''
    hidden_text=request.GET.get('text', 'default')

    tick = request.GET.get('check', 'off')
    tick1 = request.GET.get('check1', 'off')
    tick2 = request.GET.get('check2', 'off')
    tick3 = request.GET.get('check3', 'off')
    tick4 = request.GET.get('check4', 'off')
    if tick == 'on': 
        value=''
        for char in hidden_text:
            if char not in punctuation:
                value = value + char
        params = {'key':value,'chk':'box'}
       
    # if tick1 == 'on': 
    #     value=''
    #     for index, char1 in enumerate(hidden_text):
    #         if hidden_text[index] == " " and hidden_text[index + 1] == " ":
    #             value = value + 
    #     params = {'key':value,'chk':'box'}
    #     return render(request, 'analyze.html', params)
    
    if tick2 == 'on': 
        new = ''
        for v in value:
            new= new + v.upper()
        value = new
        
        # for char2 in value:
        #         value = value + char2.upper()
        params = {'key':value,'chk':'box'}
        # return render(request, 'analyze.html', params)
    
    if tick3 == 'on': 
        new1 = ''
        for k in value:
            if k != ' ':
              new1 = new1 + k
        value = new1
        params = {'key':value,'chk':'box'}
        # return render(request, 'analyze.html', params)
    
    if tick4 == 'on': 
        value=len(value)
        params = {'key':value,'chk':'box'}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse(hidden_text)