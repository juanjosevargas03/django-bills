from django.contrib import admin
from .models import Clients,Bills,Products,Bills_Products

# Register your models here.

admin.site.register(Clients)
admin.site.register(Bills)
admin.site.register(Products)
admin.site.register(Bills_Products)