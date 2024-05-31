from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name = 'register'),
    path('personal_console/<str:user_name>', views.personal_console, name = 'personal_console'),
    path('personal_console/mail/', views.get_name, name='mail'),
    path('personal_console/mails/', views.get_names, name='mails'),
    path('personal_console/gr/<int:user_id>', views.gr, name = "gr"),
    #path('personal_console/writer/<str:file_name>', views.show_file_name, name = 'file_name'),
    path('personal_console/send/<str:subject>/<str:message>/<str:name>/<yourmail>/<user_id>', views.send, name='sendmail'),
    path('sends_email/', views.get_names, name = 'sends_email'),
]