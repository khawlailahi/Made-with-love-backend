from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions

#importinf models of tables 
from .models import Seller
from .models import Buyer
from .models import Category


class signupSeller(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        email = data['email']
        password = data['password']
        store_name = data['storeName']
        location = data['location']
        category = data['category']
        description = data['description']
        delivery_time = data ['delieveryTime']
        image = data ['url']
        #check if email exsists
        obj = Seller.objects.filter(email = email)
        if obj :
            return Response ({'error':"Email already exist"})
        else:
            user = Seller.objects.create_user(email = email, store_name = store_name , password = password, description=description, delivery_time=delivery_time, image=image, location=location, category=category)
            # user.save()
            return Response ({'success':'Seller registered'})

class signupBuyer(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        email = data['email']
        password = data['password']
        username = data['userName']
        phonenumber = data['phoneNumber']
        location=data['location']
        #check if email exsists
        obj = Buyer.objects.filter(email = email)
        if obj :
            return Response ({'error':"Email already exist"})
        else:
            user =Buyer.objects.create_user(email=email, username=username , location=location, phonenumber=phonenumber, password=password)
            return Response ({'success':"Buyer registered"})


        
