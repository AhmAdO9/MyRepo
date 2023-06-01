from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . models import *
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.


@api_view(['POST'])
def post(request):
    m = request.data
    for d in m:
        serializer_obj = SerializersDashboard(data=d)
        if not serializer_obj.is_valid():
            return Response({"message": serializer_obj.errors})
        serializer_obj.save()
    return Response({"message": "done"})



def get(request):

    return render(request, "template.html")


def get1(request):
    detail = Details.objects.all()
    # jar1 = []
    jar2 = []
    # jar3 = []
    # jar4 = []
    # jar5 = []
    # jar6 = []
    jar7 = []
    # jar8 = []

    for k1 in detail:
        if  not (k1.end_year and k1.intensity and k1.start_year and k1.relevance and k1.likelihood and k1.topic and k1.country and  k1.region == ""):
            # jar1.append(k1.start_year)
            # jar7.append(f"{k1.country}/{k1.end_year}")
            # jar7.append(k1.end_year)
            # jar2.append(int(k1.intensity))
            # jar2.append(int(k1.relevance))
            jar2.append(int(k1.likelihood))
            # jar6.append(k1.topic)
            # jar8.append(k1.region)
            
    return render(request, "main.html",{"jar2":jar2})


def getNew(request):
    data = Details.objects.filter(topic = "strategy", country = "United States of America", end_year = 2026 )
    return HttpResponse(data)

  