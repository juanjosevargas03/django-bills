from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserManager,Clients,Products,Bills,Bills_Products
from .serializers import ClientSerializer,ProductSerializer,BillSerializer,Bills_ProductSerializer
import json

# Create your views here.

class Register(APIView):
    
    def post(self,request):
        jd = json.loads(request.body)
        email = jd['email']
        password = jd['password']

        user = UserManager.create_user(UserManager,email,password)

        return Response(status = status.HTTP_200_OK,data = {'message':'User created successfully'})

class ClientsView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
        
    def get(self, request,id=0):
        if(id>0):
            clients = Clients.objects.filter(id=id).all()
            if len(clients) > 0:
                client = clients[0]
                client = ClientSerializer(client)
                datos = {'message': "Success",'client': client.data}
            else:
                datos = {'message': "client not found ..."}
            return Response(datos)
        else:
            queryset = Clients.objects.all()
            serializer = ClientSerializer(queryset,many=True)
            return Response(serializer.data)

    def post(self, request):
        jd = json.loads(request.body)
        Clients.objects.create(
            document=jd['document'],
            first_name=jd['first_name'],
            last_name=jd['last_name'],
            email=jd['email'],)

        datos = {'message':"Success"}
        return Response(datos)


    def put(self, request,id):
        jd = json.loads(request.body)
        clients = list(Clients.objects.filter(id=id).values() )
        if len(clients) > 0:
            client = Clients.objects.get(id=id)
            client.document=jd['document']
            client.first_name=jd['first_name']
            client.last_name=jd['last_name']
            client.email=jd['email']
            client.save()
            client = ClientSerializer(client)

            datos = {'message':"Success",'client': client.data}
        else:
            datos = {'message': "client not found ..."}
        return Response(datos)

    def delete(self, request,id):
        clients = list(Clients.objects.filter(id=id).values() )
        if len(clients) > 0:
            Clients.objects.filter(id=id).delete() 
            datos = {'message':"Success"}
        else:
            datos = {'message': "Company not found ..."}
        return Response(datos)

class ProductsView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
        
    def get(self, request,id=0):
        if(id>0):
            products = Products.objects.filter(id=id).all()
            if len(products) > 0:
                product = products[0]
                product = ProductSerializer(product)
                datos = {'message': "Success",'product': product.data}
            else:
                datos = {'message': "product not found ..."}
            return Response(datos)
        else:
            queryset = Products.objects.all()
            serializer = ProductSerializer(queryset,many=True)
            return Response(serializer.data)

    def post(self, request):
        jd = json.loads(request.body)
        Products.objects.create(
            name=jd['name'],
            description=jd['description'],)

        datos = {'message':"Success"}
        return Response(datos)


    def put(self, request,id):
        jd = json.loads(request.body)
        products = list(Products.objects.filter(id=id).values() )
        if len(products) > 0:
            product = Products.objects.get(id=id)
            product.name=jd['name']
            product.description=jd['description']
            product.save()
            product = ProductSerializer(product)

            datos = {'message':"Success",'product': product.data}
        else:
            datos = {'message': "product not found ..."}
        return Response(datos)

    def delete(self, request,id):
        products = list(Products.objects.filter(id=id).values() )
        if len(products) > 0:
            Products.objects.filter(id=id).delete() 
            datos = {'message':"Success"}
        else:
            datos = {'message': "Company not found ..."}
        return Response(datos)

class BillsView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
        
    def get(self, request,id=0):
        if(id>0):
            bills = Bills.objects.filter(id=id).all()
            if len(bills) > 0:
                bill = bills[0]
                bill = BillSerializer(bill)
                datos = {'message': "Success",'bill': bill.data}
            else:
                datos = {'message': "client not found ..."}
            return Response(datos)
        else:
            queryset = Bills.objects.all()
            serializer = BillSerializer(queryset,many=True)
            return Response(serializer.data)

    def post(self, request):
        jd = json.loads(request.body)
        clients = Clients.objects.filter(id=jd['client_id']).all()
        if len(clients) > 0:
                client = clients[0]
        else:
               return Response({'message': "client not found ..."})

        Bills.objects.create(
            company_name=jd['company_name'],
            nit=jd['nit'],
            code=jd['code'],
            client_id=client,)

        datos = {'message':"Success"}
        return Response(datos)

    def put(self, request,id):
        jd = json.loads(request.body)

        clients = Clients.objects.filter(id=jd['client_id']).all()
        if len(clients) > 0:
                client = clients[0]
        else:
               return Response({'message': "client not found ..."})

        bills = list(Bills.objects.filter(id=id).values() )

        if len(bills) > 0:
            bill = Bills.objects.get(id=id)
            bill.company_name=jd['company_name']
            bill.nit=jd['nit']
            bill.code=jd['code']
            bill.client_id=client
            bill.save()
            bill = BillSerializer(bill)

            datos = {'message':"Success",'bill': bill.data}
        else:
            datos = {'message': "bill not found ..."}
        return Response(datos)

    def delete(self, request,id):
        bills = list(Bills.objects.filter(id=id).values() )
        if len(bills) > 0:
            Bills.objects.filter(id=id).delete() 
            datos = {'message':"Success"}
        else:
            datos = {'message': "bill not found ..."}
        return Response(datos)

class Bills_ProductsView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
        
    def get(self, request,id=0):
        if(id>0):
            bills_products = Bills_Products.objects.filter(id=id).all()
            if len(bills_products) > 0:
                bill_product = bills_products[0]
                bill_product = Bills_ProductSerializer(bill_product)
                datos = {'message': "Success",'bill': bill_product.data}
            else:
                datos = {'message': "bill_product not found ..."}
            return Response(datos)
        else:
            queryset = Bills_Products.objects.all()
            serializer = Bills_ProductSerializer(queryset,many=True)
            return Response(serializer.data)

    def post(self, request):
        jd = json.loads(request.body)
        bills = Bills.objects.filter(id=jd['bill_id']).all()
        if len(bills) > 0:
                bill = bills[0]
        else:
               return Response({'message': "bill not found ..."})

        products = Products.objects.filter(id=jd['product_id']).all()
        if len(products) > 0:
                product = products[0]
        else:
               return Response({'message': "product not found ..."})

        Bills_Products.objects.create(
            bill_id=bill,
            product_id=product,)

        datos = {'message':"Success"}
        return Response(datos)

    def put(self, request,id):
        jd = json.loads(request.body)

        bills = Bills.objects.filter(id=jd['bill_id']).all()
        if len(bills) > 0:
                bill = bills[0]
        else:
               return Response({'message': "bill not found ..."})

        products = Products.objects.filter(id=jd['product_id']).all()
        if len(products) > 0:
                product = products[0]
        else:
               return Response({'message': "product not found ..."})

        bills_products = list(Bills_Products.objects.filter(id=id).values() )

        if len(bills_products) > 0:
            bill_product = Bills_Products.objects.get(id=id)
            bill_product.bill_id=bill
            bill_product.product_id=product
            bill_product.save()
            bill_product = Bills_ProductSerializer(bill_product)

            datos = {'message':"Success",'bill_product': bill_product.data}
        else:
            datos = {'message': "bill_product not found ..."}
        return Response(datos)

    def delete(self, request,id):
        bills_products = list(Bills_Products.objects.filter(id=id).values() )
        if len(bills_products) > 0:
            Bills_Products.objects.filter(id=id).delete() 
            datos = {'message':"Success"}
        else:
            datos = {'message': "bill_product not found ..."}
        return Response(datos)

# class Logout(APIView):
#     def get(self,request, format = None):
#         request.user.auth_token.delete() # elimina token
#         logout(request) # cierra la sesion
#         return Response(status = status.HTTP_200_OK)