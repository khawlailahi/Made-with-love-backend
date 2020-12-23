from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
import json as JSON
from django.core.serializers import json
import jwt,json

#importinf models of tables 
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category

class getCategoryStore (APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, cat):
        # data = self.request.data  
        print(cat)
        obj = Seller.objects.filter(category = 'food')
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)
        # print(data)
        return Response (data)


class addItem(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data 
        print(data)

        productName = data['product'] 
        description = data['description'] 
        price = data['price']
        category = data['category']
        image = data['url'] 

        if category == "clothes":
            gender = data['gender'] 
            size = data['size'] 
            category_id = Category.objects.get(category_id =200)
            item = Item.objects.create (productname = productName, description=description, price=price, gender=gender, size=size, image=image, category=200)
            return Response ({'success': 'Add Item'})
        if(category == 'food'):
            types = data['type'] 
            category_id = Category.objects.get(category_id =100) 
            item = Item.objects.create (productname = productName, description=description, price=price,types=types, image=image, category_id=100)
            return Response ({'success': 'Add Item'})
        if category == 'accessories':
            material = data['material'] 
            category_id = Category.objects.get(category_id =300)
            item = Item.objects.create (productname = productName, description=description, price=price, image=image, material=material, category=300)
            return Response ({'success': 'Add Item'})
        if category == 'baby products':
            gender = data['gender']
            category_id = Category.objects.get(category_id =400)
            item = Item.objects.create (productname = productName, description=description, price=price, gender=gender, image=image, category=400)
            return Response ({'success': 'Add Item'})

        # category_id = data['category_id']
        # store_id = data['store_id'] 
        # item = Item.objects.create (productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
        # item.save()
        



