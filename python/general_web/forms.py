from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    #file = forms.FileField()
    class Meta:
        model = Topic
        #fields = ['text','file']
        #labels = {'text': '','file':''}
        fields = ['file']
        labels = {'file':''}


#class EmailForm(forms.ModelForm):
#    class Meta:
#        model = Topic
#        fields = ['file_mail']
#        labels = {'file_mail':''}
