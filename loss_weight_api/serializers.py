from django.forms import widgets
from rest_framework import serializers
from loss_weight_api.models import User, CheckPoint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 
                  'gender', 
                  'age', 
                  'current_waight', 
                  'initial_waight', 
                  'email', 
                  'height', 
                  'password', 
                  'registration_date')



class CheckPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckPoint
        fields = ('date',
                  'isPlanned',
                  'weight')
