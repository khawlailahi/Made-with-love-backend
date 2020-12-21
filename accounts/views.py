from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions

#importinf models of tables 
from .models import Seller
from .models import Category


class signupSeller(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        email = data['email']
        store_name = data['storeName']
        password = data['password']
        location = data['location']
        category = data['category']
        description = data['description']
        location = data['location']
        delievery_time = data ['delieveryTime']
        image = data ['url']
        #  user = Category.objects.create(name = name)
        return Response ({'success':'receiveeed'})


        #---->> i prepared this for later (after we make sure it's working)

        # if data['userType'] === 'buyer': 
        #     username = data['username']
        #     location = data['location']
        #     phoneNumber = data['phoneNumber']
        #     if model.objects.filter(email = email).exist():
        #         return Response ({'error':"Email already exist"})
        #     else :
        #         user = model.objects.create_user (email=email, password=password, userName=username, location=location, phoneNumber=phoneNumber)
        #         user.save()
        #         return Response ({'success': 'user created'})

        # if data['userType'] === 'seller': 
        #     storeName = data['storeName']
        #     description = data['description']
        #     location = data['location']
        #     delievaryTime = data['delievaryTime']
        #     image = data['image']
        #     if model.objects.filter(email = email).exist():
        #         return Response ({'error':"Email already exist"})
        #     else :
        #         user = model.objects.create_user (email=email, password=password, store_Name = storeName, description=descritption,location=location, delievary-time=delievary_time )
        #         user.save()
        #         return Response ({'success': 'user created'}) 
        # else:
            # return Response ({'ERROR':"no user information provided"})
