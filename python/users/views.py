import smtplib, ssl
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from smtplib import SMTP
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string


from .models import Message, Quantity,Analytic
from .forms import NameForm
from general_web.models import Topic
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from ip2geotools.databases.noncommercial import DbIpCity

from flask import Flask, request


user_name = ""
global_user_name = user_name
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            message = Message()
            analytic = Analytic()
            user_id = request.user.id
            #message.user = new_user
            message.id = user_id
            message.save()
            analytic.id = user_id
            message.number = 100
            #analytic.send_email = 0
            #analytic.successfully_send_email = 0
            #analytic.open_email = 0
            #message.user = User()
            #User.save(request)
            message.save()
            analytic.save()
            return redirect('general_web:index')
    context = {'form': form}
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'register.html', context)

def personal_console(request,user_name):
    user_id = request.user.id
    print (user_id)
    print (user_name)
    #message = Message()
    #message.user = user_id
    #message.save()
    mess = Message.objects.get(id = user_id)
    anl = Analytic.objects.get(id = user_id)
    #mess = Message.objects.get(user = user_name)
    #mess = 1
    topic = Quantity.objects.filter(number = user_id)  # LIMIT
    #entries = topic.entry_set.order_by('-date_added')
    context = {'user_id':user_id,'mess':mess,'topic': topic, 'anl':anl}
    return render(request, 'console.html',context)


def send(request,subject,message,name, yourmail,user_id,template):
    #boss_email = ['p_k7@mail.ru']
    boss_email = [yourmail]
    #send_mail(subject,message,'fast_mail_bot@mail.ru',boss_email)
    #send_mail(subject,message,'fast_mail_bot@mail.ru',boss_email, fail_silently=False)
    update_type = str(template)
    current_context ={'username': 'User1'}
    path = 'registration/'+str(user_id)+str(update_type)+".txt"
    text_content = get_template(path).render(current_context)
    html_content = get_template(path).render(current_context)
    from_email = 'fast_mail_bot@mail.ru'
    msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
    msg.attach_alternative(html_content, "text/html")
    res = msg.send()
    print (res)
    #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
    #email.send(fail_silently=True)
    html_content = message
    send_resault = "Сообщение доставлено"
    a.successfully = a.successfully + 1
    a.save()
    a = Message.objects.get(id = user_id)
    a.number = a.number - 1
    a.save()
    context = {
        'message':message,
        'name':name,
    }
    return render (request, 'console.html', context)

def get_name2(self, *args, **options):
        subject = "Вам письмо!"
        current_context ={'username': 'User1'}
        text_content = get_template('registration/email.txt').render(current_context)
        html_content = get_template('registration/email.txt').render(current_context)
        from_email = 'fast_mail_bot@mail.ru'
        msg = EmailMultiAlternatives(subject, text_content, from_email, ['p_k7@mail.ru'])
        msg.attach_alternative(html_content, "text/html")
        res = msg.send()
        print (res)

def get_names(request):
    print ("get_names")
    user_id = request.user.id
    user_mail = ""
    send_resault = ""
    message = ""
    send_emails = 0
    successfully_send_emails = 0
    current_date = datetime.now().date()
    current_datetime = datetime.now()
    anl = Analytic.objects.get(id = user_id)
    model_data = anl.data
    model_time = anl.time
    update_type = request.POST.get('update_type')
    topic = Quantity.objects.filter(number = user_id)  # LIMIT
    print (user_id)
    if request.method == 'POST':
        form = NameForm(request.POST)
        print ("From valid")
        if form.is_valid():
            user_mail = form.cleaned_data.get("your_name")
            print ("From valid")
            user_id = request.user.id
            mess = Message.objects.get(id = user_id)
            a = Message.objects.get(id = user_id)
            a.number = a.number - 1
            a.save()
            a.sent_number = a.sent_number + 1 
            a.save()
            print ("A")
            print (a) # Проверить работу цикла!
            user_mail = user_mail.split(";")
            for item in user_mail:
                print(item)
                a = Message.objects.get(id = user_id)
                a.number = a.number - 1
                a.save()
                a.sent_number = a.sent_number + 1
                a.save()
                print (a)
                send_emails += 1 # send_emails += 1
                print ("SEND_EMAILS!!!!")
                print (send_emails)
                print ("SEND_EMAILS!!!")
                boss_email = [item]
                subject = "hi"
                subject = "Тема для вашего письма"
                current_context ={'username': 'User1'}
                path = 'registration/'+str(user_id)+str(update_type)+'.txt'
                text_content = get_template(path).render(current_context)
                html_content = get_template(path).render(current_context)
                from_email = 'easy_fast_mail@mail.ru'
                msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
                msg.attach_alternative(html_content, "text/html")
                res = msg.send()
                print("RES")
                print (res)
                html_content = message
                send_resault = "Сообщение доставлено"
                a.successfully = a.successfully + 1
                a.save()
                successfully_send_emails += 1
            anl.send_email = str(send_emails) + ',' + str(anl.send_email)
            anl.save()
            anl.successfully_send_email = str(successfully_send_emails) + ',' + str(anl.successfully_send_email)
            anl.save()
            anl.data =  str(current_date) + ','+ str(model_data) # Сохраняем дату
            anl.save()
            minute = current_datetime.minute
            minute = str(minute)
            if len(minute) == 1:
                minute = "0" + minute
            anl.time = str(current_datetime.hour) +":"+ str(minute) + ',' + str(model_time)
            anl.save()
            return redirect('/users/personal_console/admin')
    else:
        form = NameForm()
    context = {
        'form': form,
        'topic': topic,
    }
    return render(request, 'send_form.html', context)

def get_name(request):
    #if this is a POST request we need to process the form data
    user_id = request.user.id
    user_mail = ""
    send_resault = ""
    message = ""
    update_type = request.POST.get('update_type')
    print('update_type')
    path = 'registration/'+str(user_id)+str(update_type)+".txt"
    #with open(path) as user_file:
    #    for line in user_file:
    #        message += line
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            mess = Message.objects.get(id = user_id)
            a = Message.objects.get(id = user_id)
            a.number = a.number - 1
            a.save()
            a.sent_number = a.sent_number + 1
            a.save()
            print (a)
            try:
                user_mail = form.cleaned_data.get("your_name")
                boss_email = [user_mail]
                subject = "hi"
                subject = "Тема для вашего письма"
                current_context ={'username': 'User1'}
                path = 'registration/'+str(user_id)+str(update_type)+".txt"
                text_content = get_template(path).render(current_context)
                html_content = get_template(path).render(current_context)
                from_email = 'fast_mail_bot@mail.ru'
                msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
                msg.attach_alternative(html_content, "text/html")
                res = msg.send()
                print (res)
                #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
                #email.send(fail_silently=True)
                html_content = message
                send_resault = "Сообщение доставлено"
                a.successfully = a.successfully + 1
                a.save()
                return redirect('/users/personal_console/admin')
            except:
                send_resault = "Сообщение не доставлено!"
                return redirect('/users/personal_console/admin')
    else:
        form = NameForm()
    context = {
        'user_mail':user_mail,
        'form': form,
        'send_resault':send_resault,

    }
    return render(request, 'console.html', context)

def send_mail2(user_mail):
    #server = SMTP(host="smtp.mail.ru",port="25")
    server = smtplib.SMTP_SSL(host="smtp.mail.ru",port="465")
    fromaddr = "fast_mail_bot@mail.ru"
    toaddr = user_mail
    text = user_mail
    okey = "Сообщение отправленно"

    #try:
    #server.connect(host="smtp.mail.ru", port="465")
    helo = server.helo() # Здароваемся
    print (server)
    print (helo)
    ehlo = server.ehlo() # check echo
    print (ehlo)
    tls = server.starttls() # connect to tls encryption
    print (tls)
    login = server.login(user="fast_mail_bot@mail.ru", password="ddjZQif9qA1sQ87tG38k") # login
    print (login)

    print ("i send email")
    send_mail = server.sendmail(fromaddr,toaddr,text)
    print (send_mail)
    server.quit()
    return okey

    #except:
       # error = "Ошибка"
       # return error

def gr(request,user_id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    a = Message.objects.get(id = user_id)
    a.open_ip = a.open_ip + 1
    ip = '1'
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        print(ip)
        a.ip = a.ip +'/'+ ip
        a.save()
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        a.ip = a.ip +'/'+ ip
        a.save()
    #response = DbIpCity.get(ip, api_key='free')
    #city = response.city
    a.country = "city"
    a.save()



'''
import smtplib, ssl
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from smtplib import SMTP
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Message, Quantity
from .forms import NameForm
from general_web.models import Topic

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from flask import Flask, request


user_name = ""
global_user_name = user_name
user_id = 0
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            message = Message(commit=False)
            if message.user_id is None:
                message.user_id = new_user.id
            message.save()
            user_id = request.user.id
            #message.user = new_user
            message.id = user_id
            message.save()
            message.number = 100
            #message.user = User()
            #User.save(request)
            message.save()
            return redirect('general_web:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def personal_console(request,user_name):
    user_id = request.user.id
    print (user_id)
    print (user_name)
    #message = Message()
    #message.user = user_id
    #message.save()
    mess = Message.objects.get(id = user_id)
    #mess = Message.objects.get(user = user_name)
    #mess = 1
    topic = Quantity.objects.filter(number = user_id)  # LIMIT
    #entries = topic.entry_set.order_by('-date_added')
    context = {'user_id':user_id,'mess':mess,'topic': topic}
    return render(request, 'registration/console.html',context)


def send(request,subject,message,name, yourmail,user_id,template):
    #boss_email = ['p_k7@mail.ru']
    boss_email = [yourmail]
    #send_mail(subject,message,'fast_mail_bot@mail.ru',boss_email)
    #send_mail(subject,message,'fast_mail_bot@mail.ru',boss_email, fail_silently=False)
    update_type = str(template)
    current_context ={'username': 'User1'}
    path = 'registration/'+str(user_id)+str(update_type)+".txt"
    text_content = get_template(path).render(current_context)
    html_content = get_template(path).render(current_context)
    from_email = 'fast_mail_bot@mail.ru'
    msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
    msg.attach_alternative(html_content, "text/html")
    res = msg.send()
    print (res)
    #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
    #email.send(fail_silently=True)
    html_content = message
    send_resault = "Сообщение доставлено"
    a.successfully = a.successfully + 1
    a.save()
    a = Message.objects.get(id = user_id)
    a.number = a.number - 1
    a.save()
    context = {
        'message':message,
        'name':name,
    }
    return render (request, 'registration/console.html', context)

def get_name2(self, *args, **options):
        subject = "Тема для вашего письма"
        current_context ={'username': 'User1'}
        text_content = get_template('registration/email.txt').render(current_context)
        html_content = get_template('registration/email.txt').render(current_context)
        from_email = 'fast_mail_bot@mail.ru'
        msg = EmailMultiAlternatives(subject, text_content, from_email, ['p_k7@mail.ru'])
        msg.attach_alternative(html_content, "text/html")
        res = msg.send()
        print (res)

def get_names(request):
    user_id = request.user.id
    user_mail = ""
    send_resault = ""
    message = ""
    update_type = request.POST.get('update_type')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_mail = form.cleaned_data.get("your_name")
            user_id = request.user.id
            mess = Message.objects.get(id = user_id)
            a = Message.objects.get(id = user_id)
            a.number = a.number - 1
            a.save()
            a.sent_number = a.sent_number + 1
            a.save()
            print (a)
            user_mail = user_mail.split(";")
            for item in user_mail:
                print(item)
                user_id = request.user.id
                mess = Message.objects.get(id = user_id)
                a = Message.objects.get(id = user_id)
                a.number = a.number - 1
                a.save()
                a.sent_number = a.sent_number + 1
                a.save()
                print (a)
                try:
                    #user_mail = form.cleaned_data.get("your_name")
                    boss_email = [item]
                    subject = "hi"
                    subject = "Тема для вашего письма"
                    current_context ={'username': 'User1'}
                    path = 'registration/'+str(user_id)+str(update_type)+".txt"
                    text_content = get_template(path).render(current_context)
                    html_content = get_template(path).render(current_context)
                    from_email = 'fast_mail_bot@mail.ru'
                    msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
                    msg.attach_alternative(html_content, "text/html")
                    res = msg.send()
                    print (res)
                    #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
                    #email.send(fail_silently=True)
                    html_content = message
                    send_resault = "Сообщение доставлено"
                    a.successfully = a.successfully + 1
                    a.save()
                    #return redirect('/users/personal_console/admin')
                except:
                    send_resault = "Сообщение не доставлено!"
                    #return redirect('/users/personal_console/admin')
            return redirect('/users/personal_console/admin')
    else:
        form = NameForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/console.html', context)

def get_name(request):
    #if this is a POST request we need to process the form data
    user_id = request.user.id
    user_mail = ""
    send_resault = ""
    message = ""
    update_type = request.POST.get('update_type')
    print('update_type')
    path = 'registration/'+str(user_id)+str(update_type)+".txt"
    #with open(path) as user_file:
    #    for line in user_file:
    #        message += line
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            mess = Message.objects.get(id = user_id)
            a = Message.objects.get(id = user_id)
            a.number = a.number - 1
            a.save()
            a.sent_number = a.sent_number + 1
            a.save()
            print (a)
            try:
                user_mail = form.cleaned_data.get("your_name")
                boss_email = [user_mail]
                subject = "hi"
                subject = "Тема для вашего письма"
                current_context ={'username': 'User1'}
                path = 'registration/'+str(user_id)+str(update_type)+".txt"
                text_content = get_template(path).render(current_context)
                html_content = get_template(path).render(current_context)
                from_email = 'fast_mail_bot@mail.ru'
                msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
                msg.attach_alternative(html_content, "text/html")
                res = msg.send()
                print (res)
                #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
                #email.send(fail_silently=True)
                html_content = message
                send_resault = "Сообщение доставлено"
                a.successfully = a.successfully + 1
                a.save()
                return redirect('/users/personal_console/admin')
            except:
                send_resault = "Сообщение не доставлено!"
                return redirect('/users/personal_console/admin')
    else:
        form = NameForm()
    context = {
        'user_mail':user_mail,
        'form': form,
        'send_resault':send_resault,

    }
    return render(request, 'registration/console.html', context)

def send_mail2(user_mail):
    #server = SMTP(host="smtp.mail.ru",port="25")
    server = smtplib.SMTP_SSL(host="smtp.mail.ru",port="465")
    fromaddr = "fast_mail_bot@mail.ru"
    toaddr = user_mail
    text = user_mail
    okey = "Сообщение отправленно"

    #try:
    #server.connect(host="smtp.mail.ru", port="465")
    helo = server.helo() # Здароваемся
    print (server)
    print (helo)
    ehlo = server.ehlo() # check echo
    print (ehlo)
    tls = server.starttls() # connect to tls encryption
    print (tls)
    login = server.login(user="fast_mail_bot@mail.ru", password="ddjZQif9qA1sQ87tG38k") # login
    print (login)

    print ("i send email")
    send_mail = server.sendmail(fromaddr,toaddr,text)
    print (send_mail)
    server.quit()
    return okey

    #except:
       # error = "Ошибка"
       # return error

def gr(request,user_id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    a = Message.objects.get(id = user_id)
    a.open_ip = a.open_ip + 1
    a.save()
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        print(ip)
        ip_check_path = 'http://ipwho.is/'+str(ip)
        x = request.get(ip_check_path)
        a.ip = a.ip +'/'+ ip
        a.save()
        a.country = a.country + '/' + x
        a.save()
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        ip_check_path = 'http://ipwho.is/'+str(ip)
        x = request.get(ip_check_path)
        a.ip = a.ip +'/'+ ip
        a.save()
        a.country = a.country + '/' + x
        a.save()
    





import smtplib, ssl
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from smtplib import SMTP
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Message, Quantity
from .forms import NameForm
from general_web.models import Topic

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from flask import Flask, request


user_name = ""
global_user_name = user_name
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('general_web:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def personal_console(request,user_name):
    user_id = request.user.id
    mess = Message.objects.get(id = user_id)
    #mess = 1
    topic = Quantity.objects.filter(number = user_id)  # LIMIT
    #entries = topic.entry_set.order_by('-date_added')
    context = {'user_id':user_id,'mess':mess,'topic': topic}
    return render(request, 'registration/console.html',context)


def send(request,subject,message,name, yourmail):
    #boss_email = ['p_k7@mail.ru']
    boss_email = [yourmail]
    #send_mail(subject,message,'fast_mail_bot@mail.ru',boss_email)
    #send_mail(subject,message,'fast_mail_bot@mail.ru',boss_email, fail_silently=False)
    email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
    email.send(fail_silently=True)
    user_id = 1
    a = Message.objects.get(id = user_id)
    a.number = a.number - 1
    a.save()
    context = {
        'message':message,
        'name':name,
    }
    return render (request, 'registration/console.html', context)

def get_name2(self, *args, **options):
        subject = "Тема для вашего письма"
        current_context ={'username': 'User1'}
        text_content = get_template('registration/email.txt').render(current_context)
        html_content = get_template('registration/email.txt').render(current_context)
        from_email = 'fast_mail_bot@mail.ru'
        msg = EmailMultiAlternatives(subject, text_content, from_email, ['p_k7@mail.ru'])
        msg.attach_alternative(html_content, "text/html")
        res = msg.send()
        print (res)

def get_names(request):
    user_id = request.user.id
    user_mail = ""
    send_resault = ""
    message = ""
    update_type = request.POST.get('update_type')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_mail = form.cleaned_data.get("your_name")
            user_id = request.user.id
            mess = Message.objects.get(id = user_id)
            a = Message.objects.get(id = user_id)
            a.number = a.number - 1
            a.save()
            a.sent_number = a.sent_number + 1
            a.save()
            print (a)
            user_mail = user_mail.split(";")
            for item in user_mail:
                print(item)
                user_id = request.user.id
                mess = Message.objects.get(id = user_id)
                a = Message.objects.get(id = user_id)
                a.number = a.number - 1
                a.save()
                a.sent_number = a.sent_number + 1
                a.save()
                print (a)
                try:
                    #user_mail = form.cleaned_data.get("your_name")
                    boss_email = [item]
                    subject = "hi"
                    subject = "Тема для вашего письма"
                    current_context ={'username': 'User1'}
                    path = 'registration/'+str(user_id)+str(update_type)+".txt"
                    text_content = get_template(path).render(current_context)
                    html_content = get_template(path).render(current_context)
                    from_email = 'fast_mail_bot@mail.ru'
                    msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
                    msg.attach_alternative(html_content, "text/html")
                    res = msg.send()
                    print (res)
                    #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
                    #email.send(fail_silently=True)
                    html_content = message
                    send_resault = "Сообщение доставлено"
                    a.successfully = a.successfully + 1
                    a.save()
                    #return redirect('/users/personal_console/admin')
                except:
                    send_resault = "Сообщение не доставлено!"
                    #return redirect('/users/personal_console/admin')
            return redirect('/users/personal_console/admin')
    else:
        form = NameForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/console.html', context)


def get_name(request):
    #if this is a POST request we need to process the form data
    user_id = request.user.id
    user_mail = ""
    send_resault = ""
    message = ""
    update_type = request.POST.get('update_type')
    print('update_type')
    path = '/registration/'+str(user_id)+str(update_type)+".txt"
    #with open(path) as user_file:
    #    for line in user_file:
    #        message += line
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            mess = Message.objects.get(id = user_id)
            a = Message.objects.get(id = user_id)
            a.number = a.number - 1
            a.save()
            a.sent_number = a.sent_number + 1
            a.save()
            print (a)
            try:
                user_mail = form.cleaned_data.get("your_name")
                boss_email = [user_mail]
                subject = "hi"
                subject = "Тема для вашего письма"
                current_context ={'username': 'User1'}
                path = 'registration/'+str(user_id)+str(update_type)+".txt"
                text_content = get_template(path).render(current_context)
                html_content = get_template(path).render(current_context)
                from_email = 'fast_mail_bot@mail.ru'
                msg = EmailMultiAlternatives(subject, text_content, from_email,boss_email)
                msg.attach_alternative(html_content, "text/html")
                res = msg.send()
                print (res)
                #email = EmailMessage(subject,message,'fast_mail_bot@mail.ru',boss_email)
                #email.send(fail_silently=True)
                html_content = message
                send_resault = "Сообщение доставлено"
                a.successfully = a.successfully + 1
                a.save()
                return redirect('/users/personal_console/admin')
            except:
                send_resault = "Сообщение не доставлено!"
                return redirect('/users/personal_console/admin')
    else:
        form = NameForm()
    context = {
        'user_mail':user_mail,
        'form': form,
        'send_resault':send_resault,

    }
    return render(request, 'registration/console.html', context)

def send_mail2(user_mail):
    #server = SMTP(host="smtp.mail.ru",port="25")
    server = smtplib.SMTP_SSL(host="smtp.mail.ru",port="465")
    fromaddr = "fast_mail_bot@mail.ru"
    toaddr = user_mail
    text = user_mail
    okey = "Сообщение отправленно"

    #try:
    #server.connect(host="smtp.mail.ru", port="465")
    helo = server.helo() # Здароваемся
    print (server)
    print (helo)
    ehlo = server.ehlo() # check echo
    print (ehlo)
    tls = server.starttls() # connect to tls encryption
    print (tls)
    login = server.login(user="fast_mail_bot@mail.ru", password="ddjZQif9qA1sQ87tG38k") # login
    print (login)

    print ("i send email")
    send_mail = server.sendmail(fromaddr,toaddr,text)
    print (send_mail)
    server.quit()
    return okey

    #except:
       # error = "Ошибка"
       # return error

def gr(request,user_id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    a = Message.objects.get(id = user_id)
    a.open_ip = a.open_ip + 1
    a.save()
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        print(ip)
        a.ip = a.ip +'/'+ ip
        a.save()
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        a.ip = a.ip +'/'+ ip
        a.save()
    return render(request, 'registration/register.html')
'''