from rest_framework import serializers
from .models import UserData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields=('id','name','age','contact','address')
