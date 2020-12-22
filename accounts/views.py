

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from .models import Item


# class signupSeller(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         data = self.request.data  
#         email = data['email']
#         store_name = data['storeName']
#         password = data['password']
#         # store_Name= data['name']
#         cat = Category.objects.create(name=name)
#         cat.save()
#         return Response ({'success':'lololoolleshh'})
#         # return Response ({'success':'receiveeed'})
#         location = data['location']
#         category = data['category']
#         description = data['description']
#         location = data['location']
#         delievery_time = data ['delieveryTime']
#         image = data ['url']
#         #  user = Category.objects.create(name = name)
#         return Response ({'success':'receiveeed'})


        # ---->> i prepared this for later (after we make sure it's working)

        # if data['userType'] == 'buyer': 
        #     username = data['username']
        #     location = data['location']
        #     phoneNumber = data['phoneNumber']
        #     if Buyer.objects.filter(email = email).exist():
        #         return Response ({'error':"Email already exist"})
        #     else :
        #         user = Buyer.objects.create_user(email=email, password=password, username=username, location=location, phonenumber=phoneNumber)
        #         user.save()
        #         return Response ({'success': 'user created'})

        # if data['userType'] == 'seller': 
        #     store_name = data['storeName']
        #     description = data['description']
        #     location = data['location']
        #     delievaryTime = data['delievaryTime']
        #     image = data['image']
        #     if Seller.objects.filter(email = email).exist():
        #         return Response ({'error':"Email already exist"})
        #     else :
        #         user = Seller.objects.create_user(email=email, password=password, store_name = store_name, description=descritption,location=location, delievary_time=delievaryTime )
        #         user.save()
        #         return Response ({'success': 'user created'}) 
        # else:
        #     return Response ({'ERROR':"no user information provided"})

