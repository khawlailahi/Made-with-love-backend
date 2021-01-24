# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, store_name  , description, delivery_time, image, location, category, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        s = 'gh@f$#$@&4hjhgjh'
        e = '786huyh8%3h'
        length = (len(password)/2)
        iy = int(length)
        print(length)
        firstpart = password[0:iy]
        seconedpart = password[iy:len(password)]
        x =password[0] + s + firstpart[1:int(len(firstpart)/2)] + s + firstpart[int(len(firstpart)/2):] + seconedpart[:int(len(seconedpart)/2)] + e + seconedpart[int(len(seconedpart)/2):]
        user = self.model(email=email,  store_name = store_name , password = x, description=description, delivery_time=delivery_time, image=image, location=location, category=category)
        user.save()
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class Seller(AbstractBaseUser, models.Model):
    store_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=110)
    password = models.CharField(max_length=45)
    store_name = models.CharField(max_length=45)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    delivery_time = models.CharField(db_column='delivery_time', max_length=45)  # Field renamed to remove unsuitable characters.
    image = models.TextField()
    category=models.CharField(max_length=45)
    objects =  UserAccountManager()
    USERNAME_FIELD = 'email'
    class Meta:

        db_table = 'seller'

class BuyerAccountManager(BaseUserManager):
    def create_user(self, email, username , location, phonenumber,is_active,password=None ):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        if not password : 
            print(email)
            user = self.model(email=email, username=username , location=None, phonenumber=None, password=None, is_active=True)
            user.save()
            return user
        s = 'gh@f$#$@&4hjhgjh'
        e = '786huyh8%3h'
        length = (len(password)/2)
        iy = int(length)
        print(length)
        firstpart = password[0:iy]
        seconedpart = password[iy:len(password)]
        x =password[0] + s + firstpart[1:int(len(firstpart)/2)] + s + firstpart[int(len(firstpart)/2):] + seconedpart[:int(len(seconedpart)/2)] + e + seconedpart[int(len(seconedpart)/2):]
        user = self.model(email=email, username=username , location=location, phonenumber=phonenumber, password=x, is_active=True)
        user.save()
        return user

class Buyer(AbstractBaseUser,models.Model):
    buyer_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=110)
    password = models.CharField(max_length=45)
    username = models.CharField(db_column='userName', unique=True, max_length=45)  # Field name made lowercase.
    location = models.CharField(max_length=100)
    phonenumber = models.IntegerField(db_column='phoneNumber')  
    is_active = models.BooleanField(default=True)
    objects =  BuyerAccountManager()
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def __str__(self):
        return self.email
    class Meta:

        db_table = 'buyer'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:

        db_table = 'category'


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    productname = models.CharField(db_column='productName', max_length=45)  # Field name made lowercase.
    description = models.CharField(max_length=233)
    price = models.IntegerField()
    gender = models.CharField(max_length=45, blank=True, null=True)
    types = models.CharField(max_length=45, blank=True, null=True)
    size = models.CharField(max_length=45)
    image = models.TextField()
    material = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey(Seller,db_column='store_id', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'item'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    store = models.ForeignKey(Seller,on_delete= models.CASCADE)

    store = models.ForeignKey(Seller, on_delete= models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    phonenumber = models.IntegerField(db_column='phoneNumber')  # Field name made lowercase.
    order_date = models.CharField(max_length=45)
    delievery_date = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    is_payed = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        db_table = 'order'


class Comments(models.Model):
    commentsid = models.AutoField(db_column='commentsID', primary_key=True)  # Field name made lowercase.
    comment = models.CharField(max_length=300)
    iditem = models.IntegerField(db_column='IDitem', blank=True, null=True)  # Field name made lowercase.
    idbuyer = models.IntegerField(db_column='IDbuyer', blank=True, null=True)  # Field name made lowercase.
    idstore = models.IntegerField(db_column='IDstore', blank=True, null=True)  # Field name made lowercase.
    types = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = ' comments'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review = models.CharField(max_length=45, blank=True, null=True)
    store = models.ForeignKey(Seller, db_column='store_id',on_delete= models.CASCADE, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
   
    class Meta:
        db_table = 'review'
