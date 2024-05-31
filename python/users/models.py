from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Analytic(models.Model):
    #data = models.DateField(null=True)
    data = models.CharField(max_length=1000, null=True,default="")
    time = models.CharField(max_length=1000, null=True,default="")
    send_email = models.CharField(max_length=1000, null=True)
    successfully_send_email = models.CharField(max_length=1000, null=True)
    open_email = models.CharField(max_length=1000, null=True)

class Message(models.Model):
    """Колличество оставшихся сообщений"""
    number = models.IntegerField(null=True, default=0) # Количество сообщений
    may = models.IntegerField( null=True, default=0)
    sent_number = models.IntegerField(default=0,null=True)
    successfully = models.IntegerField(default=0,null=True)
    ip = models.CharField(max_length=2000, default = "", null=True)
    open_ip = models.IntegerField(default=0,null=True)
    country = models.CharField(max_length=200, default="", null=True)
    analytics_id = models.ForeignKey(Analytic,  on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # Внешний ключ - пользователь
    #other = models.TextField()
    #def __str__(self):
    #    return self.other

class Quantity(models.Model):
    number = models.IntegerField() # Колличество шаблонов
    name_file = models.CharField(max_length=20000)
    name = models.CharField(max_length=200)
    number_for_summ = models.IntegerField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

