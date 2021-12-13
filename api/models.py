from django.db import models
from django.contrib.auth.models import BaseUserManager,User

class UserManager(BaseUserManager):

    def create_user(self,email,password):
        if not email:
            raise ValueError('El email es obligatorio')

        #email = BaseUserManager.normalize_email(email)
        user = User(username=email,email=email)
        user.set_password(password)
        user.save() 
        return user 

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    client_id = models.ForeignKey(Clients,null=False,blank=False, on_delete=models.CASCADE)


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Bills_Products(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bills,null=False,blank=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,null=False,blank=False, on_delete=models.CASCADE)
