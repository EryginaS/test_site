from rest_framework import serializers
from bboard.models import Applications, ItPerson


class ItPersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItPerson
        fields = ['first_name', 'last_name']


class ApplicationsSerializer(serializers.ModelSerializer):
    
    responsible = ItPersonSerializer()
    
    class Meta:
        model = Applications
        fields = '__all__'
        


        
    