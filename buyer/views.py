from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
import json as JSON
from django.core.serializers import json
#importinf models of tables 
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category


class getCategoryItems(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, cat):
        # data = self.request.data  
        print(cat)
        obj = Seller.objects.filter(category = 100)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)
        # print(data)
        return Response (data)
        # print(json_serialized)
        # print(JSON.loads(json_serialized))
        # myData = []
        # class MyClass:
        #      id = 5
        #      info = ""
        # obj1 = MyClass()
        # for x in data:
        #     obj1.id=x['pk']
        #     obj1.info=x['fields']
        #     # setattr(x, 'id', x['pk'])
        #     # x['fields'].id = x['pk']
        #     myData.append(obj1)
        # print(myData)
        
        