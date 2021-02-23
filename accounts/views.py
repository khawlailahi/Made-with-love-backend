from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
import jwt
from django.http import HttpResponse
import json 
from django.core.serializers import json as JSON
import codecs
from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from django.http import HttpResponse

from .models import Seller
from .models import Item
from .models import Buyer
from .models import Category
from .models import Comments
from .models import Review

class signup_seller(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        email = data['email']
        password = data['password']
        store_name = data['storeName']
        location = data['location']
        category = data['category']
        description = data['description']
        delivery_time= data ['delieveryTime']
        image = data ['url']
        #check if email exsists
        obj = Seller.objects.filter(email = email)
        tr1 = Seller.objects.filter(email = email)

        if obj or tr1:
            return Response ({'error':"Email already exist"})
        else:
            user = Seller.objects.create_user(email = email, store_name = store_name , password = password, description=description, delivery_time=delivery_time, image=image, location=location, category=category)
            # user.save()
            return Response ({'success':'Seller registered'})


class signup_buyer(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data  
        email = data['email']
        password = data['password']
        username = data['userName']
        phonenumber = data['phoneNumber']
        location=data['location']
        try:
            obj = Buyer.objects.get(email = email)
            if obj:
                return HttpResponse({"Email already exist"}, status = "403")
        except Buyer.DoesNotExist:
            if not data['password'] :
                payload = {
                            'email': email,
                    }
                tok = jwt.encode(payload, "SECRET_KEY")
                user =Buyer.objects.create_user(email=email, username=username , location=location, phonenumber=phonenumber, password=password, is_active = True)
                userId = Buyer.objects.get(email =  email )
                jwt_token = {'token': jwt.encode(payload, "SECRET_KEY"),"is_store":userId.buyer_id, "type":"buyer"}
                return Response(jwt_token)
            else:
                user =Buyer.objects.create_user(email=email, username=username , location=location, phonenumber=phonenumber, password=password, is_active = True)
                return Response ({'success':"Buyer registered"})



class login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        email = request.data['email']
        password = request.data['password']
        try:
            Seller.objects.get(email = email)         
            Buyer.objects.get(email = email)
        except Buyer.DoesNotExist:
            try:
                userSeller = Seller.objects.get(email=email)
                password = self.request.data['password']
                 
                s = 'gh@f$#$@&4hjhgjh'
                e = '786huyh8%3h'
                r ="".join(userSeller.password.split(s))
                t = "".join(r.split(e))
                if t == self.request.data['password']:
                    payload = {
                        'email': userSeller.email,
                    }
                    tok = jwt.encode(payload, "SECRET_KEY")
                    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY"),"id":userSeller.store_id, "type":"seller"}
                    return Response(jwt_token)


            except Seller.DoesNotExist :
                return HttpResponse({'Error': "Invalid credentials"} ,  status ="400")
        except Seller.DoesNotExist:
            try:
                userBuyer = Buyer.objects.get(email=email)
            
                password = self.request.data['password']
                if not password:
                    payload = {
                            'email': userBuyer.email,
                    }
                    tok = jwt.encode(payload, "SECRET_KEY")
                    jwt_token = {'token': tok,"id_store":userBuyer.buyer_id, "type":"buyer"}
                    return Response(jwt_token)
                elif password:
                    userBuyer = Buyer.objects.get(email=email)
                    s = 'gh@f$#$@&4hjhgjh'
                    e = '786huyh8%3h'
                    r ="".join(userBuyer.password.split(s))
                    t = "".join(r.split(e))
                    if t == self.request.data['password']:
                        payload = {
                            'email': userBuyer.email
                        }
                    jwt_token = {'token': jwt.encode({
                            'email': userBuyer.email
                        }, "SECRET_KEY"),"id_store":userBuyer.buyer_id, "type":"buyer"}
                    return Response(jwt_token)
            except Buyer.DoesNotExist :
                return HttpResponse({"Invalid credentials"}, status ="400")
        else :
            return Response(
            json.dumps({ "Invalid credentials"}),
            status=400,
            content_type="application/json"
            )


class comment(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = self.request.data  
        print(data)
        text = data['text']
        user_id = data ['user_id']
        item_id = data['item_id']
        types = data['types']
        if types == 'seller':
            user = Seller.objects.get(store_id =user_id )
            username = user.store_name
        if types == 'buyer':
            user = Buyer.objects.get(buyer_id =user_id )
            username = user.username
        item = Item.objects.get(item_id = item_id )
        store = Seller.objects.get(store_id = item.store_id )
        Comments.objects.create(comment = text , iditem = item_id, idbuyer = user_id, idstore = store.store_id , types=types)
        return Response( {"username" : username })
        
class get_comments(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,id):
        data = Comments.objects.filter(iditem = id)
        json_serializer = JSON.Serializer()
        json_serialized = json_serializer.serialize(data)
        data= json.loads(json_serialized)
        
        for x in data:      
            if x["fields"]["types"] == "buyer" :
                y=Buyer.objects.get(buyer_id = x["fields"]["idbuyer"] )
                x["fields"]["buyer"] =y.username
            if x["fields"]["types"] == "seller" :
                y=Seller.objects.get(store_id = x["fields"]["idbuyer"] )
                x["fields"]["buyer"] =y.store_name
        return Response(data)


class delete_comment(APIView):
    permission_classes = (permissions.AllowAny,)  
    def delete(self, request, pk, format=None):
        Comments.objects.filter(pk=pk).delete()
        return Response('Deleteeeed')

#get the stores that have reviews
class most_populer (APIView):
    permission_classes = (permissions.AllowAny,)  
    def get(self, request, format=None):
        data = Review.objects.all()
        json_serializer = JSON.Serializer()
        json_serialized = json_serializer.serialize(data)
        data= json.loads(json_serialized)
        for x in data:
            store = Seller.objects.get(store_id = x["fields"]["store"])
            x["fields"]["store_name"] = store.store_name
            x["fields"]["image"] = store.image
            x["fields"]["description"] = store.description
        return Response(data)

        # return HttpResponse( json_serializer.serialize(data), status ="200")
