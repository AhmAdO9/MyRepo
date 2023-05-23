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
        if not k1.end_year == '':
            if not k1.intensity == '':
                if not k1.start_year == '':
                    if not k1.relevance == '':
                        if not k1.likelihood == '':
                            if not k1.topic == '':
                                if not k1.country == '':
                                    if not k1.region == '':

                                        # jar1.append(k1.start_year)
                                        # jar7.append(f"{k1.country}/{k1.end_year}")
                                        # jar7.append(k1.end_year)
                                        # jar2.append(int(k1.intensity))
                                        # jar2.append(int(k1.relevance))
                                        jar2.append(int(k1.likelihood))
                                        # jar6.append(k1.topic)
                                        # jar8.append(k1.region)
                                       

                                    else:
                                        pass

                                else:
                                    pass

                            else:
                                pass

                        else:
                            pass

                    else:
                        pass
                else:
                    pass

            else:
                pass

        else:
            pass

            # for j1 in jar1:


                

    return render(request, "main.html",{"jar2":jar2})


def getNew(request):
    data = Details.objects.filter(topic = "strategy", country = "United States of America", end_year = 2026 )
    return HttpResponse(data)

  
    
    #                 else:
    #                     pass

    # for k in output:
    #     if k != '':
    #         jar.append(int(k))
    #         jar1.append(int(k1))
    #         # `  jar.append(int(k))
    #         #    jar1.append(int(k1))
    #     else:
    #         pass

    # else:
    # pass

    # return HttpResponse(f" {jar1}:{jar}")
    #  ``````for k in output:
    #    `````  `  if k =='':
    #      ``````       pass
    #    ``````` ` else:
    #    ``````````    jar.append(int(k))
    #    ``````````    jar1.append(int(k1))
    # # jar1 = [u for u in k]
    # return HttpResponse(f" {jar1}:{jar}")

    #     # output1 = ",".join([z.intensity for z in detail])
    # return render(request, "template.html", {"detail":output})

    # output = [y.relevance for y in detail]
    # jar = []
    # for k in output:
    #     if k =='':
    #         pass
    #     else:
    #      jar.append(int(k))
    # output2 = [y.intensity for y in detail]
    # if not output1 and output2 == '':
    #     jar1 = []
    #     jar2=[]
    #     for k in output1:
    #         jar1.append(int(k))
    #         for k2 in output2:
    #           jar2.append(int(k2))
    # else:

#    jar1 = jar1 + (f"""  "start_year":{k1.start_year},"end_year":{k1.end_year},"intensity":{k1.intensity},"relevance":{k1.relevance},"likelihood":{k1.likelihood} """)
# def new(request):
