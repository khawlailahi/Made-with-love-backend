from django.shortcuts import render
from django.http import HttpResponse
import json as JSON
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from django.core.serializers import json
import jwt

#importing models of tables
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Review
from accounts.models import Order


#get stores by category
class get_category_store (APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, cat):
        obj = Seller.objects.filter(category = cat)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)
        return Response (data)

        
class add_item(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        productName = data['product']
        description = data['description']
        price = data['price']
        category = data['category']
        image = data['url']
        store1 = data['user']
        
        if category == "clothes":
            gender = data['gender']
            size = data['size']
            category_id = Category.objects.get(category_id =200)
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            item = Item.objects.create (productname = productName, store_id=s, description=description, price=price, gender=gender, size=size, image=image, category=200)
            return HttpResponse({'success': 'Add Item'} ,status="200")
        if(category == 'food'):
            types = data['type']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =100)
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price,types=types, image=image, category_id=100)
            return HttpResponse({'success': 'Add Item'} ,status="200")
        if category == 'accessories':
            material = data['material']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =300)
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, image=image, material=material, category=300)
            return HttpResponse({'success': 'Add Item'} ,status="200")
        if category == 'babyproducts':
            gender = data['gender']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =400)
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, gender=gender, image=image, category=400)
            return HttpResponse({'success': 'Add Item'} ,status="200")

       
class get_items(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj) 
         data= JSON.loads(json_serialized)
         for x in data:
             z= Seller.objects.get(store_id = x["fields"]["store"] )
             x["fields"]["storeId"]=x["fields"]["store"]
             x["fields"]["store"] = z.store_name
         return Response(data)


class get_items_visit(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         data= JSON.loads(json_serialized)
         for x in data:
             z= Seller.objects.get(store_id = x["fields"]["store"] )
             x["fields"]["store_id"] = x["fields"]["store"]
             x["fields"]["store"] = z.store_name
         return Response(data)

class seller_visit(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
        obj1 = Seller.objects.filter(pk=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        myData = []
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        myData.append(json_serialized1)
        myData.append(json_serialized)
        return Response(json_serialized1)

class delete_item(APIView):
    permission_classes = (permissions.AllowAny,)  
    def delete(self, request, pk, format=None):
        Item.objects.filter(pk=pk).delete()
        print('Deleeeete')
        return Response('Deleteeeed')

class get_rate (APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    email = tole['email']
                    try :
                        buyerEmail = Buyer.objects.get( email = email)   
                        x = Order.objects.filter(store=pk , buyer=buyerEmail.buyer_id)
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(x)

                        if  len(json_serialized) != 0 and len(json_serialized) !=2:  
                            try:
                                review = Review.objects.get(store_id =pk)
                                returnVal = {'true':True , "ratee":review.review }
                                return Response(returnVal)
                            except Review.DoesNotExist :
                                return Response({'true':True})
                        if len(json_serialized) == 0 or len(json_serialized) == 2:
                            try :
                                review = Review.objects.get(store_id =pk)
                                return Response({'false':False,"ratee":review.review  })
                            except Review.DoesNotExist:
                                return Response({'false':False})

                    except Buyer.DoesNotExist:
                        seller = Seller.objects.get( email = email)
                        try:
                            review = Review.objects.get(store_id =pk)
                            return Response({'false':False,"ratee":review.review  })
                        except Review.DoesNotExist:
                            return Response({'false':False})
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")









class snippet_detail_seller(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request,pk, format=None):
        print(pk)
        obj1 = Seller.objects.filter(pk=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        myData = []
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        myData.append(json_serialized1)
        myData.append(json_serialized)
        return Response(json_serialized1)

class get_list_order (APIView):
     permission_classes = (permissions.AllowAny,)
     def get(self, request, pk):
         store = Seller.objects.get(store_id=pk)
         store = store.store_name
         obj= Order.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         data= JSON.loads(json_serialized)
         for x in data:
             y=Item.objects.get(item_id = x["fields"]["item"] )
             x["fields"]["item"] =y.productname
             z=Buyer.objects.get(buyer_id = x["fields"]["buyer"] )
             x["fields"]["buyer"]= z.username
             x["store"] = store
         return Response (data)


class  seller_password(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         newPassword = data['newPassword']
         password = data['oldPassword']
         user = Seller.objects.get(email= tole)
         print(password,"new" )
         
         s = 'gh@f$#$@&4hjhgjh'
         e = '786huyh8%3h'
         r ="".join(user.password.split(s))
         t = "".join(r.split(e))
         print (t,"db")
         
         if password == t:
             s = 'gh@f$#$@&4hjhgjh'
             e = '786huyh8%3h'
             length = (len(newPassword)/2)
             iy = int(length)
             print(length)
             firstpart = newPassword[0:iy]
             seconedpart = newPassword[iy:len(newPassword)]
             x =newPassword[0] + s + firstpart[1:int(len(firstpart)/2)] + s + firstpart[int(len(firstpart)/2):] + seconedpart[:int(len(seconedpart)/2)] + e + seconedpart[int(len(seconedpart)/2):]
             Seller.objects.filter(email= tole).update(password =x)
             return HttpResponse({"success":"password changed"} ,status="200")
         else:
            return HttpResponse({"Unauthorized":"password incorrect"} ,status="400")

class  seller_storename(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         storeName= data['storeName']
         Seller.objects.filter(email= tole).update(store_name =storeName )
         return HttpResponse({"success":"location changed"} ,status="200") 

class edit_item (APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, pk):
        data = self.request.data
        if not data:
            return HttpResponse({"Error":"please enter your information"} ,status="401")
        elif data:
            try:
                gender = data['gender']
                size = data['size']
                productName = data['product']
                description = data['description']
                price = data['price']
                image = data['url']
                material = data['material']
                types = data['type']
                image = data['url']
                Item.objects.filter(item_id= pk).update(productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
                return HttpResponse({"success":"updated"} ,status="200")
            except Item.DoesNotExist:
                return HttpResponse({"Error":"ERROR"} ,status="401")

#changing seller settings 
class  seller_location(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         location= data['location']
         Seller.objects.filter(email= tole).update(location =location )
         return HttpResponse({"success":"location changed"} ,status="200")


class  seller_delivery(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         delivery= data['delivery']
         Seller.objects.filter(email= tole).update(delivery_time =delivery )
         return HttpResponse({"success":"delivery time changed"} ,status="200")


class  seller_image(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         image= data['image']
         Seller.objects.filter(email= tole).update(image =image )
         return HttpResponse({"success":"location changed"} ,status="200")

class  seller_description(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         description= data['description']
         Seller.objects.filter(email= tole).update(description =description )
         return HttpResponse({"success":"description changed"} ,status="200")

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
                    obj11 = Seller.objects.filter(email = email)
                    if obj11:
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj11)
                        data1= JSON.loads(json_serialized)
                        return Response (data1)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        