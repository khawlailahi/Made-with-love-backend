from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate


#importinf models of tables 
from .models import Seller
from .models import Buyer
from .models import Category
import json as JSON
from django.contrib.auth.hashers import check_password

class signupSeller(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        print(data)
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
            user =Buyer.objects.create_user(email=email, username=username , location=location, phonenumber=phonenumber, password=password, is_active = True)
            return Response ({'success':"Buyer registered"})


# class Login(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request):
#         if not request.data:
#             return Response({'Error': "Please provide username/password"}, status="400")
#         email = request.data['email']
#         password = request.data['password']
#         try:
#             user = Seller.objects.get(email=email)

#             print() 
#         except Seller.DoesNotExist:
#             return Response({'Error':'nooo'}, status="400")
#         if :
#             payload = {
#                 'email': user.email,
#             }
#             jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
#             return Response( JSON.dumps(jwt_token),
#               status=200,
#               content_type="application/json")
#         else:
#             return Response(
#               JSON.dumps({'Error': "Invalid credentials"}),
#               status=400,
#               content_type="application/json"
#             )




        
