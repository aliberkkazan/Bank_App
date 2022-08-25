from django.shortcuts import render
from customer_account.models import customer,account
from customer_account.api.serializer import accountSerializer, customerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.shortcuts import get_object_or_404


#  Creating customers list api view
class customerListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
   
    def get(self,request):
        if request.user.has_perm('customer_account.view_customer')  is True:
            customers = customer.objects.all()
            serializer= customerSerializer(customers,many=True)
            return Response(serializer.data)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to view customer!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )

    def post(self,request):
        if request.user.has_perm('customer_account.view_customer')  is True:
            serializer=customerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to view customer!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )
#  Creating accounts list api view
class accountListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        if request.user.has_perm('customer_account.view_account')  is True:
            accounts = account.objects.all()
            serializer= accountSerializer(accounts,many=True)
            return Response(serializer.data)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to view accounts!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )
    def post(self,request):
        if request.user.has_perm('customer_account.add_account')  is True:
            serializer=accountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to add accounts!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )
#  Creating customers for call with id
class customerDetailAPIView(APIView):


    def get_object(self,pk):
        customer_instance=get_object_or_404(customer,pk=pk)
        return customer_instance
    
    def get(self,request,pk):
        customer=self.get_object(pk=pk)
        serializer=customerSerializer(customer)
        return Response(serializer.data)
    
    def put(self,request,pk):
        if request.user.has_perm('customer_account.change_customer')  is True:
            customer=self.get_object(pk=pk)
            serializer=customerSerializer(customer,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to change customer!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )
  

    def delete(self,request,pk):
        if request.user.has_perm('customer_account.delete_customer')  is True:
            customer=self.get_object(pk=pk)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to delete customer!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )
#  Creating customers for call with id
class accountDetailAPIView(APIView):

    def get_object(self,pk):
        account_instance=get_object_or_404(account,pk=pk)
        return account_instance
    
    def get(self,request,pk):
        account=self.get_object(pk=pk)
        serializer=accountSerializer(account)
        return Response(serializer.data)
    
    def put(self,request,pk):
        if request.user.has_perm('customer_account.change_account')  is True:
            account=self.get_object(pk=pk)
            serializer=accountSerializer(account,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to change account!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )
  

    def delete(self,request,pk):
        if request.user.has_perm('customer_account.delete_account')  is True:
            account=self.get_object(pk=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {
                    'errors':{
                        'code':403,
                        'message':f'You dont have permission to delete account!'
                    }
                },
                status=status.HTTP_403_FORBIDDEN
            )

