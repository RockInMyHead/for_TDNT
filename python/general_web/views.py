from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.

from users.models import Quantity

def index(request):
    return render(request,'general_web/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'general_web/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'general_web/topic.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/writers/')
    #return render(request,'general_web/index.html')

# Загрузка файлов

def handle_uploaded_file(f, user_id):
    #quant = Quantity.objects.get(id = user_id)
    #quant.name_file = f
    #quant.save()
    #quants = quant.number + 1
    #quant.number = quants 
    #quant.save()
    qua = Quantity()
    qua.number = user_id
    qua.name_file = f
    #qua.user = user_id
    #quants = qua.number_for_summ + 1
    qua.number_for_summ = qua.number
    print (user_id)
    #number = int(user_id)
    #qua.user = number
    qua.save()
    print ("Колличество шаблонов")
    #print (quants)
    path = 'users/templates/registration/'+str(user_id)+str(f)+".txt"
    code = []
    my_code = []
    magic_code = []
    magic_src = '<img src = "http://easyfastmail.ru/users/personal_console/gr/' + str(user_id) +'">'
    #path = 'first_app/users/templates/registration/'+str(user_id)+str(f)+".txt"
    print (f)
    for chunk in f.chunks():
        code = chunk.split()
    for item in code:
        item_2 = item.decode()
        my_code.append(item_2)
    for item in my_code:
        if item == "<body>":
            magic_code.append(item + '\r')
            magic_code.append(magic_src + '\r')
        else:
            magic_code.append(item + '\r')
    with open(path,'w') as file:
        for items in magic_code:
            file.write(items)
    """
    for item in code:
        if item == b'<body>':
            my_code.append(item)
            my_code.append(magic_src)
        else:
            my_code.append(item)
    for item in my_code:
        print (item)
    with open (path, 'wb+') as file:
        for item in my_code:
            file.write(item)

    with open(path,'w') as file:
        for item in code:
            if item == '<body>\n':
                file.write(magic_src)
            item = item + str("\r\n")
            file.write(item)
   
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open(path, 'r') as file:
        user_code = file.readlines()
        print (user_code)
    with open(path,'wb+') as file:
        for item in user_code:
            if item == '<body>\n':
                file.write(magic_src)
            file.write(item)
    """
def new_topic(request):
    user_id = request.user.id
    print ("USER_ID")
    print (user_id)
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], user_id)
            #form.save()
            return HttpResponseRedirect('/writers/')
    else:
        form = TopicForm()
    return render(request, 'general_web/new_topic.html', {'form': form})

#def new_topic(request):  # its has mistaiks
#    if request.method != 'POST':
#        form = TopicForm()
#    else:
#        form = TopicForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            return render(request, 'general_web/writers.html')
#    context = {'form':form}
#    return render(request, 'general_web/new_topic.html', context)


def writers(request):
    user_id = request.user.id
    topic = Quantity.objects.filter(number = user_id)  # LIMIT
    #entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic}
    return render(request, 'general_web/writers.html',context)


def writer(request, file_name):
    print (file_name)
    user_id = request.user.id
    code = Quantity.objects.filter(number = user_id, name_file = file_name)  # LIMIT
    #code = topic.objects.filter(name = file_name)
    print (code)
    user_code = "d"
    path = 'users/templates/registration/'+str(user_id)+str(file_name)+".txt"
    print (path)
    with open(path, 'r') as file:
            user_code = file.readlines()
    context = {
        'code':code,
        'user_code':user_code

        }
    return render (request, 'general_web/writer.html', context)



"""from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

from users.models import Quantity

def index(request):
    return render(request,'general_web/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'general_web/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'general_web/topic.html', context)

# Загрузка файлов

def handle_uploaded_file(f, user_id):
    #quant = Quantity.objects.get(id = user_id)
    #quant.name_file = f
    #quant.save()
    #quants = quant.number + 1
    #quant.number = quants 
    #quant.save()
    qua = Quantity()
    qua.number = user_id
    qua.name_file = f
    #qua.user = user_id
    #quants = qua.number_for_summ + 1
    qua.number_for_summ = qua.number
    print (user_id)
    #number = int(user_id)
    #qua.user = number
    qua.save()
    print ("Колличество шаблонов")
    #print (quants)
    path = 'first_app/users/templates/registration/'+str(user_id)+str(f)+".txt"
    magic_src = '<img src = "https://easyfastmail.ru/users/personal_console/gr/2">'
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            if (chunk == '<body>'):
                destination.write(magic_src)
            destination.write(chunk)

def new_topic(request):
    user_id = request.user.id
    print ("USER_ID")
    print (user_id)
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], user_id)
            #form.save()
            return HttpResponseRedirect('/writers/')
    else:
        form = TopicForm()
    return render(request, 'general_web/new_topic.html', {'form': form})

#def new_topic(request):  # its has mistaiks
#    if request.method != 'POST':
#        form = TopicForm()
#    else:
#        form = TopicForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            return render(request, 'general_web/writers.html')
#    context = {'form':form}
#    return render(request, 'general_web/new_topic.html', context)


def writers(request):
    user_id = request.user.id
    topic = Quantity.objects.filter(number = user_id)  # LIMIT
    #entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic}
    return render(request, 'general_web/writers.html',context)


def writer(request, file_name):
    print (file_name)
    user_id = request.user.id
    code = Quantity.objects.filter(number = user_id, name_file = file_name)  # LIMIT
    #code = topic.objects.filter(name = file_name)

    print (code)
    context = {'code':code}
    return render (request, 'general_web/writer.html', context)"""