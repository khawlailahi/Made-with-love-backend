from django.shortcuts import render

# Create your views here.
import json as JSON
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from accounts.models import Item
from accounts.models import Seller
from django.core.serializers import json





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



class getItems(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,pk, format=None):
         print('eeeeeeeeeeeeeeeeeeeeeeeeee')
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         print(json_serialized,"iteeeeeems" )
         return Response(json_serialized)

class getItemsVisit(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,pk, format=None):
         print('eeeeeeeeeeeeeeeeeeeeeeeeee')
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         print(json_serialized,"iteeeeeems" )
         return Response(json_serialized)


class sellerVisit(APIView):
    permission_classes = (permissions.AllowAny,)         

    def get(self, request,pk, format=None):
        
        print(pk)
        obj1 = Seller.objects.filter(pk=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        # print(json_serialized )
        myData = []
        print(pk,">>>>11111111111111")
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        # print(json_serialized )
        myData.append(json_serialized1)
        myData.append(json_serialized)
        print("mydataaa",myData,"dataaend")
        # dat =   JSON.dumps(myData)
        return Response(json_serialized1)         

class SnippetDetailSeller(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.AllowAny,)
    # def get(self,request,  pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    # def get(self, request,pk, format=None):
    #      print('eeeeeeeeeeeeeeeeeeeeeeeeee')
    #      obj = Seller.objects.filter(pk=pk)
    #      json_serializer = json.Serializer()
    #      json_serialized = json_serializer.serialize(obj)
    #      print(json_serialized )
    #      return Response(json_serialized)

    def get(self, request,pk, format=None):
        
        print(pk)
        #   data = self.request.data 
        # store_Name = data['store_Name'] 
        # description = data['description'] 
        # location = data['location'] 
        # delivery_date = data[' delivery_date '] 
        # image = data['image']
        # category_id = data['category_id']
        # store_id = data['store_id'] 
        # serializer = SnippetSerializer(snippet)
        obj1 = Seller.objects.filter(pk=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        # print(json_serialized )
        myData = []
        print(pk,">>>>11111111111111")
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        # print(json_serialized )
        myData.append(json_serialized1)
        myData.append(json_serialized)
        print("mydataaa",myData,"dataaend")
        # dat =   JSON.dumps(myData)
        return Response(json_serialized1)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)