from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import HttpResponse
import json as JSON
import jwt
from django.core.serializers import json
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Review
from accounts.models import Order

class order_item(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
            tole = jwt.decode(token, "SECRET_KEY")['email'] 
            buyer = Buyer.objects.get(email = tole)
            order = data['order']
            item_id = data['item_id']
            is_payed=data['is_payed']
            if is_payed == True:
                pay = "Payed With credit Card "
            if is_payed == False:
                pay = "Unpayed"
            phonenumber = order['phoneNumber']
            quantity=order['quantity']
            location =data['location']
            storename=data['store_id']
            date=data['date']
            seller = Seller.objects.get(store_name = storename)
            item= Item.objects.get(item_id = item_id)
            price= item.price
            total = price * int(quantity)
            orders= Order.objects.create(buyer_id = buyer.buyer_id, quantity=quantity, store_id=seller.store_id, item_id=item_id, phonenumber=phonenumber, order_date=date, location=location, price = total , is_payed=pay )
            return HttpResponse({"success":"ordered"} ,status="200")
        
class get_category_items(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, cat):
        if cat == 'food':
            category = 100
        if cat == 'clothes':
            category = 200
        if cat == 'babyproducts':
            category = 400
        if cat == 'accessories':
            category = 300
        obj = Item.objects.filter(category = category)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)

        for x in data:
                y=Seller.objects.get(store_id = x["fields"]["store"] )
                x["fields"]["id"] = x["fields"]["store"]
                x["fields"]["store"] =y.store_name
        return Response (data)

#when a buyer review / rate a store that he ordred from 
class rate(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'])
                    email = tole['email']
                    buyerID = Buyer.objects.get(email = email)
                    print(buyerID,"kkkkkkkkkkkkkkkkkk")
                    data = self.request.data
                    rate = data['rate']
                    storeID= data['pkSeller']
                    seller = Seller.objects.get(store_id = storeID)
                    print(seller,"uiiiiiii")
                    try:
                        print("i'm innnn")
                        review = Review.objects.get(store=seller)
                        print(review.review)
                        if rate == 1:
                            num = 20
                        if rate == 2 :
                            num = 40
                        if rate == 3 :
                            num = 60
                        if rate == 4:
                            num = 80
                        if rate == 5:
                            num = 100
                        calculationRev = int(review.review)
                        rating =  calculationRev + num
                        counter =  review.counter + 1
                        final = round(rating/counter)
                        Review.objects.filter(store=seller).update(review = final, store=seller,counter = counter)
                        return Response({"rate":final})
                    except Review.DoesNotExist:
                        if rate == 1:
                            num = 20
                        if rate == 2 :
                            num = 40
                        if rate == 3 :
                            num = 60
                        if rate == 4:
                            num = 80
                        if rate == 5:
                            num = 100
                        Review.objects.create(review = num, counter = 1, store=seller )
                        return HttpResponse({"rate" :num} ,status="200")
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")






 #changing buyer password       
class  buyer_password(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         password = data['oldPassword']
         newPassword = data['newPassword']
         user = Buyer.objects.get(email= tole)
         s = 'gh@f$#$@&4hjhgjh'
         e = '786huyh8%3h'
         r ="".join(user.password.split(s))
         t = "".join(r.split(e))
         
         if password == t:
             s = 'gh@f$#$@&4hjhgjh'
             e = '786huyh8%3h'
             length = (len(newPassword)/2)
             iy = int(length)
             firstpart = newPassword[0:iy]
             seconedpart = newPassword[iy:len(newPassword)]
             x =newPassword[0] + s + firstpart[1:int(len(firstpart)/2)] + s + firstpart[int(len(firstpart)/2):] + seconedpart[:int(len(seconedpart)/2)] + e + seconedpart[int(len(seconedpart)/2):]
             Buyer.objects.filter(email= tole).update(password =x )
             return HttpResponse({"success":"password changed"} ,status="200")
         else:
            return HttpResponse({"Unauthorized":"password incorrect"} ,status="400")

 #changing buyer username        
class  buyer_username(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         username= data['userName']
         Buyer.objects.filter(email= tole).update(username =username )
         return HttpResponse({"success":"username changed"} ,status="200")

 #changing buyer location
class  buyer_location(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         location= data['location']
         Buyer.objects.filter(email= tole).update(location =location )
         return HttpResponse({"success":"location changed"} ,status="200")

 #changing buyer phone number
class buyer_number(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         phoneNumber= data['phoneNumber']
         Buyer.objects.filter(email= tole).update(phonenumber = phoneNumber)
         return HttpResponse({"success":"location changed"} ,status="200")

class get_all(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    email = tole['email']
                    obj11 = Buyer.objects.filter(email = email)
                    if obj11:
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj11)
                        data1= JSON.loads(json_serialized)
                        return Response (data1)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")