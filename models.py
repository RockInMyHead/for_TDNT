from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Внешний ключ - пользователь
    file = models.FileField(null=True)
    #file_mail = models.FileField(null=True)
    # изменить модель и сделать миграцию для решения ошибки с нот нулл
    def __str__(self):
        return self.text
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."