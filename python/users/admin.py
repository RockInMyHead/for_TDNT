from django.contrib import admin

# Register your models here.

from .models import Message, Quantity,Analytic
admin.site.register(Message)
admin.site.register(Quantity)
admin.site.register(Analytic)