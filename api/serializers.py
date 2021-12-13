from django.db.models import fields
from rest_framework import serializers
from .models import Clients, Products, Bills, Bills_Products

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = (
            'id',
            'document',
            'first_name',
            'last_name',
            'email',
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'id',
            'name',
            'description',
        )

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = (
            'id',
            'company_name',
            'nit',
            'code',
            'client_id',
        )


class Bills_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills_Products
        fields = (
            'id',
            'bill_id',
            'product_id',
        )