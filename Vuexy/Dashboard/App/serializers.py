from .models import *
from rest_framework import serializers





class SerializersDashboard(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'



class NewDashboard(serializers.ModelSerializer):
    class Meta:
        model = DetailsNew
        fields = '__all__'