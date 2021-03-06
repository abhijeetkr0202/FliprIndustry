from django.shortcuts import render
from rest_framework import mixins,generics

from .serializers import DataSerializer
from .models import UserData
from rest_framework.response import Response

# Create your views here.

# ModelViewSet handles Get and Post

class DataView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=UserData.objects.all()
    serializer_class=DataSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class UserView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class=DataSerializer
    def get_object(self,pk):
        try:
            return UserData.objects.get(pk=pk)
        except Data.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer=DataSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer=DataSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        data=self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




import csv
from django.views.generic import View
from django.http import HttpResponse

class UserCSVexportView(View):
    serializer_class=DataSerializer

    def get_serializer(self,queryset,many=True):
        return self.serializer_class(
            queryset,
            many=many,
        )
    
    def get(self,request,*args,**kwargs):
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment;filename="user_info.csv"'

        serializer=self.get_serializer(
            UserData.objects.all(),
            many=True
        )
        header=DataSerializer.Meta.fields
        
        writer = csv.DictWriter(response,fieldnames=header)
        for row in serializer.data:
            writer.writerow(row)
        return response
