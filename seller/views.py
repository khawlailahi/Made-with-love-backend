from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from accounts.models import Item




class addItem(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data 
        productName = data['productName'] 
        description = data['description'] 
        price = data['price'] 
        gender = data['gender'] 
        types = data['types'] 
        size = data['size'] 
        image = data['image'] 
        material = data['material'] 
        # category_id = data['category_id']
        # store_id = data['store_id'] 
        item = Item.objects.create (productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
        item.save()
        return Response ({'success': 'Add Item'})