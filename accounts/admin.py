from django.contrib import admin
from .models import Product
from django.contrib import admin
from django.contrib.admin.models import LogEntry

admin.site.register(LogEntry)


# Register your models here.
admin.site.register(Product)
