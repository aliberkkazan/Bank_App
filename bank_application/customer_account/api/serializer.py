from asyncore import read
from dataclasses import fields
from datetime import date
from pyexpat import model
from unicodedata import name
from rest_framework import serializers
from customer_account.models import account, balance, customer


# customer model serializer
class customerSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField()
    class Meta:
        model = customer
        fields = '__all__'
        read_only_fields=[id,date]

# account model serializer
class accountSerializer(serializers.ModelSerializer):
    # balance=serializers.SerializerMethodField
    # def get_balance (self,obj):
    #     total=balance.objects.all()
    #     id = account.objects.get(id=id)
    #     for objects in object:
    #         if type is True:
    #             total = balance + balance.amount
    #         elif type is True:
    #             total = balance - balance.amount
    #         return total

    class Meta:
        model = account
        fields = '__all__'
        read_only_fields=[id,customer]


    
 
   
